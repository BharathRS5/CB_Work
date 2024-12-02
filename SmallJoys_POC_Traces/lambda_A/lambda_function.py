import json
import requests

def lambda_handler(event, context):
    # URL of the API Gateway that triggers Lambda B
    api_gateway_url = 'https://<api-id-b>.execute-api.<region>.amazonaws.com/prod/triggerLambdaB'

    # Data that Lambda A will send to Lambda B
    data = {
        'message': 'Hello from Lambda A'
    }

    # Make the HTTP POST request to trigger Lambda B via its API Gateway
    try:
        response = requests.post(api_gateway_url, json=data)
        response.raise_for_status()
        return {
            'statusCode': 200,
            'body': json.dumps('Lambda A triggered Lambda B successfully')
        }
    except requests.exceptions.RequestException as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
