import boto3
from botocore.exceptions import NoCredentialsError

def validate_credentials():
    session = boto3.Session()
    credentials = session.get_credentials()
    if credentials is None:
        raise NoCredentialsError("AWS credentials not found. Please configure your AWS credentials.")
    frozen = credentials.get_frozen_credentials()
    return {
        "access_key": frozen.access_key,
        "method": session.get_credentials().method,
    }