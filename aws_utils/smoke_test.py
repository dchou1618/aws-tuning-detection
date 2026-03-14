from aws_utils.aws_session import validate_credentials
from aws_utils.iam_client import IAMClient


def run_aws_smoke_test():
    print("Validating AWS credentials...")

    cred_info = validate_credentials()
    print(f"Credentials resolved via: {cred_info['method']}")

    iam = IAMClient()

    print("Testing IAM connectivity...")
    users = iam.list_users()

    print("IAM connectivity OK")
    print("Sample users:", users)