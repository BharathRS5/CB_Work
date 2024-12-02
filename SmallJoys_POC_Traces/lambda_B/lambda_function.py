import json

def lambda_handler(event, context):
    # Lambda B simply receives the data from Lambda A
    print(f"Received data: {event['message']}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Lambda B processed the data successfully')
    }
