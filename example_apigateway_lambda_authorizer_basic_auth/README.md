# example_apigateway_lambda_authorizer_basic_auth

Example SAM template showing how to implement Basic authentication in API Gateway using a Lambda authorizer.

Incorrect username/password combination returns 401 Unauthorized response from the authorizer function, otherwise the authorizer test function is invoked.

Resources created:
  - API Gateway (REST API)
  - Lambda authorizer function
  - Lambda authorizer test function