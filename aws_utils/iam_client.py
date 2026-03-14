import boto3
from botocore.exceptions import NoCredentialsError, ClientError

class IAMClient:
    def __init__(self):
        try:
            self.iam = boto3.client('iam')
        except NoCredentialsError:
            raise RuntimeError("AWS credentials not found. Please configure your AWS credentials.")
        except Exception as e:
            print(f"Error initializing IAM client: {e}")

    def list_users(self, max_items=5):
        try:
            response = self.iam.list_users(MaxItems=max_items)
            return response['Users']
        except NoCredentialsError:
            print("AWS credentials not found. Please configure your AWS credentials.")
            return []
        except ClientError as e:
            print(f"An error occurred: {e}")
            return []