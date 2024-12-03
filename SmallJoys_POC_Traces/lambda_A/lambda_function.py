import json
import requests

def lambda_handler(event, context):
    # Check the HTTP method from the event object
    http_method = event['httpMethod']
    
    if http_method == 'GET':
        # For GET request, simply return a message
        return {
            'statusCode': 200,
            'body': json.dumps('GET request triggered. This is a simple message from Lambda A.')
        }
    
    elif http_method == 'POST':
        # For POST request, trigger API Gateway 2 to invoke Lambda B
        api_gateway_url = 'https://zamv2zuy9g.execute-api.us-east-1.amazonaws.com/dev/triggerLambdaB'
        
        # Data Lambda A will send to Lambda B
        data = {
            'message': 'Hello from Lambda A'
        }

        # Send POST request to API Gateway 2
        try:
            response = requests.post(api_gateway_url, json=data)
            response.raise_for_status()  # Raise an error for non-2xx responses
            return {
                'statusCode': 200,
                'body': json.dumps('Lambda A successfully triggered Lambda B.')
            }
        except requests.exceptions.RequestException as e:
            return {
                'statusCode': 500,
                'body': json.dumps(f'Error: {str(e)}')
            }
    
    else:
        # Handle unsupported HTTP methods (optional)
        return {
            'statusCode': 405,
            'body': json.dumps('Method Not Allowed')
        }

