import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://cosmosprod2305:n4A1n60as853n6EV5WcOGr6hZPuZdbCyPIRZW6HVkt9fASKGiLt7dnCc8JmTT8QIJH21TlFds7ReACDbKsWE7w==@cosmosprod2305.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@cosmosprod2305@"  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['dev']
            collection = database['advertisements']
            
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
