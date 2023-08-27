import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "AccountEndpoint=https://cosprod23.documents.azure.com:443/;AccountKey=pyxhOW8Sg5qQJH1XYLplp1S37m9XRz0ybd3pC2P4MJ82u8tbPzt4hKX3P6qrlDW1tLcvscOpwW7VACDbDMvsQQ==;"  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['labdb']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)