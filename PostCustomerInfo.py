# Lambda function to post customer information
import json
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key

# Initialize the DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
dynamodb_table = dynamodb.Table('PlatinumPteLtd_CustomerInfo')

customer_path = '/customer'
status_check_path = '/status_PlatinumPteLtd_PostCustomerInfo'

def lambda_handler(event, context):
    print('Request event: ', event)
    response = None

    try:
        http_method = event.get('httpMethod')
        path = event.get('path')

        if http_method == 'OPTIONS':
            response = build_response(200, 'CORS preflight request')
        elif http_method == 'GET' and path == status_check_path:
            response = build_response(200, 'Service is operational')
        elif http_method == 'POST' and path == customer_path:
            response = save_customer(json.loads(event['body']))
        else:
            response = build_response(404, '404 Not Found')

    except Exception as e:
        print('Error:', e)
        response = build_response(400, 'Error processing request')

    return response

def save_customer(request_body):
    try:
        dynamodb_table.put_item(Item=request_body)
        body = {
            'Operation': 'SAVE',
            'Message': 'SUCCESS',
            'Item': request_body
        }
        return build_response(200, body)
    except ClientError as e:
        print('Error:', e)
        return build_response(400, e.response['Error']['Message'])

def build_response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,POST"
        },
        "body": json.dumps(body)
    }
