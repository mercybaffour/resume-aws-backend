import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

ddb = boto3.resource('dynamodb')
table = ddb.Table('visits')

def fetchCount(event, context):
    response = table.update_item(
        Key={
            'id': 'view-count'
        },
        UpdateExpression='SET visitorCount = visitorCount + :value',
        ExpressionAttributeValues={
            ':value':1
        },
        ReturnValues="UPDATED_NEW"
    )

    responseBody = json.dumps({"visitorCount": int(response["Attributes"]["visitorCount"])})

    apiResponse = {
        "isBase64Encoded": False,
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        "body": responseBody
    }


    # Return api response object
    return apiResponse
        
  

