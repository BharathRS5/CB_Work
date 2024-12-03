import json

def lambda_handler(event, context):
    # Lambda B processes the event from Lambda A via API Gateway 2
    message = event['message']  # Extract message sent from Lambda A
    print(f"Received message: {message}")  # You can check the logs in CloudWatch for this

    return {
        'statusCode': 200,
        'body': json.dumps(f"Lambda B received the message: {message}")
    }
