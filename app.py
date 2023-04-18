from dominio.dominio import Dominio 
import json

def handler(event, context):  
    if "body" in event:
        event = json.loads(event["body"]) 
    try: 
        Dominio.scraping()  
        return {"statusCode": 200, "message": "Ok" }
    except Exception as e: 
        return {"statusCode": 500, "message": str(e)}
