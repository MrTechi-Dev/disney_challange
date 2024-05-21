import boto3
from botocore.exceptions import ClientError

def remove_public_access_from_rds_instances():
    """Check if the RDS Instances have public access, if so, remove it to avoid undesired access."""
    region_name='us-west-2'
     # Create an RDS client with the specified region
    rds = boto3.client('rds', region_name=region_name)
    try:
        instances = rds.describe_db_instances()['DBInstances']
        # Check if the RDS instance is publicly accessible
        for instance in instances:
            if instance['PubliclyAccessible']:
                # If the instance is publicly accessible, print a message
                # and modify the instance to remove public access
                print(f"Removing public access from RDS instance: {instance['DBInstanceIdentifier']}")
                rds.modify_db_instance(
                    DBInstanceIdentifier=instance['DBInstanceIdentifier'],
                    PubliclyAccessible=False,
                    ApplyImmediately=True
                )
    except ClientError as e:
        print(f"Error processing RDS instances: {e}")

if __name__ == "__main__":
    remove_public_access_from_rds_instances()
