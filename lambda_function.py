import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ItemsTable')

def lambda_handler(event, context):
    if event['httpMethod'] == 'POST':
        item = json.loads(event['body'])
        table.put_item(Item=item)
        return {
            'statusCode': 200,
            'body': json.dumps('Item created')
        }
    elif event['httpMethod'] == 'GET':
        response = table.scan()
        return {
            'statusCode': 200,
            'body': json.dumps(response['Items'])
        }

