# Use the AWS Lambda Python 3.8 runtime as a base image
FROM public.ecr.aws/lambda/python:3.8

# Set the working directory inside the container to /var/task (this is where Lambda looks for code)
WORKDIR /var/task

# Copy the Lambda function code into the container
COPY lambda_function.py .

# Install the 'requests' library for making HTTP requests
RUN pip install requests

# Set the default command to invoke the Lambda handler
CMD ["lambda_function.lambda_handler"]
