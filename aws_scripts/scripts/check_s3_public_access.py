import boto3
import json
from botocore.exceptions import ClientError

def remove_public_access_from_s3_buckets():
    """Check if the S3 buckets have public access, if so, remove it to avoid undesired access."""
    region_name='us-west-2'
    # Create an S3 client with the specified region
    s3 = boto3.client('s3',  region_name=region_name)
    # List all buckets in the region
    response = s3.list_buckets()
    buckets = response['Buckets']
    
    # Iterate over each bucket
    for bucket in buckets:
        bucket_name = bucket['Name']
        try:
            acl = s3.get_bucket_acl(Bucket=bucket_name)
            grants = acl['Grants']
            # Iterate over each grant in the ACL
            for grant in grants:
                # If public access is found, print a message and update the bucket ACL to private
                if grant['Grantee']['Type'] == 'Group' and 'AllUsers' in grant['Grantee']['URI']:
                    print(f"Removing public access from bucket: {bucket_name}")
                    s3.put_bucket_acl(Bucket=bucket_name, ACL='private')
        except ClientError as e:
            print(f"Error processing bucket {bucket_name}: {e}")

if __name__ == "__main__":
    remove_public_access_from_s3_buckets()
