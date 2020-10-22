# example_apigateway_sqs_integration

Example SAM Template showing API Gateway-SQS integration

Resources created:
  - SQS queue
    - default settings
  - API Gateway
    - No auth
    - POST method on root resource "/"
    - Headers: 
        - X-Api-Key
        - Content-Type: application/json
  - IAM role for API Gateway to send messages to the SQS queue
  - UsagePlan
    - quota 1000 messages per month
    - burst limit ~20
  - ApiKey