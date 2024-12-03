import json
import requests

def lambda_handler(event, context):
    # URL of the API Gateway that triggers Lambda B (POST request)
    api_gateway_url_post = 'https://zamv2zuy9g.execute-api.us-east-1.amazonaws.com/dev/triggerLambdaB'
    
    # URL for a simple GET request (it could be any URL, replace with your actual URL)
    api_gateway_url_get = 'https://0e34g2ft2e.execute-api.us-east-1.amazonaws.com/dev/triggerGetEndpoint'  # Replace with actual GET URL

    # Data that Lambda A will send to Lambda B in the POST request
    data = {
        'message': 'Hello from Lambda A'
    }

    # Make the HTTP POST request to trigger Lambda B via its API Gateway
    try:
        # Trigger Lambda B via POST
        response_post = requests.post(api_gateway_url_post, json=data)
        response_post.raise_for_status()  # This will raise an error for non-2xx responses
        post_message = 'Lambda A triggered Lambda B successfully'
        print(post_message)
        
        # Now, trigger a GET request to another endpoint
        response_get = requests.get(api_gateway_url_get)
        response_get.raise_for_status()  # This will raise an error for non-2xx responses
        get_message = 'Lambda A made a GET request successfully'
        print(get_message)

        # Return the success status for both operations
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': post_message,
                'get_message': get_message
            })
        }
    except requests.exceptions.RequestException as e:
        # Handle any error that occurs during the HTTP requests
        error_message = f'Error: {str(e)}'
        return {
            'statusCode': 500,
            'body': json.dumps({'error': error_message})
        }
