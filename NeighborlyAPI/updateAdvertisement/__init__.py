import azure.functions as func
import pymongo
from bson.objectid import ObjectId

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')
    request = req.get_json()

    if request:
        try:
            url = "mongodb://cosmosprod2305:n4A1n60as853n6EV5WcOGr6hZPuZdbCyPIRZW6HVkt9fASKGiLt7dnCc8JmTT8QIJH21TlFds7ReACDbKsWE7w==@cosmosprod2305.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@cosmosprod2305@"  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['dev']
            collection = database['advertisements']
            
            filter_query = {'_id': ObjectId(id)}
            update_query = {"$set": eval(request)}
            rec_id1 = collection.update_one(filter_query, update_query)
            return func.HttpResponse(status_code=200)
        except:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)
    else:
        return func.HttpResponse('Please pass name in the body', status_code=400)

