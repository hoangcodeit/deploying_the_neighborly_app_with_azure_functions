import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "AccountEndpoint=https://cosprod23.documents.azure.com:443/;AccountKey=pyxhOW8Sg5qQJH1XYLplp1S37m9XRz0ybd3pC2P4MJ82u8tbPzt4hKX3P6qrlDW1tLcvscOpwW7VACDbDMvsQQ==;"  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['labdb']
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
