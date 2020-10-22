import logging
import base64

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """Lambda authorizer function implementing Basic Authentication."""

    # Log event data
    logger.info(event)

    # The method arn is the API resource the client is trying to access
    method_arn = event["methodArn"]

    # Get the Base64 value of the username and password
    try:
        base64_auth_value = event["headers"]["Authorization"].split()[1]
    except ValueError:
        logger.info("No Authorization header found")
        # Return 401 Unauthorized response
        raise Exception("Unauthorized")

    # Decode Base64 value to string to get username and password
    credentials_bytes = base64.b64decode(base64_auth_value)
    credentials = credentials_bytes.decode('ascii')
    username = credentials.split(":")[0]
    password = credentials.split(":")[1]

    # Check that the username and password are correct
    if username == "myusername" and password == "mypassword":
        logger.info("Credentials are correct. Returning authorized response...")
        return generate_auth_response(username, "Allow", method_arn)
    else:
        logger.info("Credentials are incorrect. Returning unauthorized response...")
        # Return 401 Unauthorized response
        raise Exception("Unauthorized")

def generate_auth_response(principal_id, effect, method_arn):

    auth_response = {
        "principalId": principal_id,
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": effect,
                    "Resource": method_arn
                }
            ]
        }
    }

    logger.info("Auth Response: {}".format(auth_response))
    return auth_response