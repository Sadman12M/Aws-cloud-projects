import json
import time
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('GuestBookMessages')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        name = body['name']
        message = body['message']

        message_id = str(int(time.time() * 1000)) # unique ID using timestamp

        table.put_item(
            Item={
                'messageId': message_id,
                'name': name,
                'message': message,
                'timestamp': time.strftime('%Y-%m-%dT%H:%M:%S')
            }
        )

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'success': True, 'message': 'Saved successfully!'})
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'success': False, 'error': str(e)})
        }