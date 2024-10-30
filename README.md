# Serverless Application with AWS Lambda

## Project Overview
This project demonstrates how to create a RESTful API using AWS Lambda and API Gateway with DynamoDB for storage. The API allows for creating and retrieving items stored in a DynamoDB table.

## Technologies
- AWS Lambda
- AWS API Gateway
- DynamoDB
- AWS SAM (Serverless Application Model)

## Setup
1. **Install AWS SAM CLI**:
   - Follow the installation instructions [here](https://docs.aws.amazon.com/serverless-application-model/latest/userguide/install-sam-cli.html).

2. **Configure AWS CLI**:
   - Set up your AWS credentials:
     ```bash
     aws configure
     ```

3. **Build the application**:
   - Run the following command to build the application:
     ```bash
     sam build
     ```

4. **Deploy the application**:
   - Deploy using:
     ```bash
     sam deploy --guided
     ```
   - This will prompt you for parameters like stack name and AWS region.

5. **Test the API**:
   - You can test the API using Postman or curl.
   - Example to create an item using `curl`:
     ```bash
     curl -X POST https://<api-id>.execute-api.<region>.amazonaws.com/Prod/items -H "Content-Type: application/json" -d '{"id": "1", "name": "Item1"}'
     ```
   - Example to retrieve items:
     ```bash
     curl -X GET https://<api-id>.execute-api.<region>.amazonaws.com/Prod/items
     ```

## API Endpoints
- `POST /items`: Create an item (send a JSON object with `id` and `name`).
- `GET /items`: Get all items stored in the DynamoDB table.

