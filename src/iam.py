import boto3

client = boto3.client('iam')
print(client.list_access_keys(UserName='your-username',
                              MaxItems=123,
                              Marker='your-marker'))