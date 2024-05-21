import boto3
from botocore.exceptions import ClientError

def remove_ssm_policy_from_ec2_instances():
    """Check if the EC2 instances have the SSM policy on their roles, if so, remove that policy from all instances."""
    region_name='us-west-2'

        #  creates EC2 and  IAM clients with specified region
    ec2 = boto3.client('ec2', region_name=region_name)
    iam = boto3.client('iam', region_name=region_name)
    try:
        instances = ec2.describe_instances()['Reservations']
        for reservation in instances:
            for instance in reservation['Instances']:
                # Check if instance has an IAM instance profile
                if 'IamInstanceProfile' in instance:
                    profile_arn = instance['IamInstanceProfile']['Arn']
                    profile_name = profile_arn.split('/')[-1]
                    # Get instance profile details from IAM
                    response = iam.get_instance_profile(InstanceProfileName=profile_name)
                    roles = response['InstanceProfile']['Roles']
                    # Iterate over roles attached to the instance profile
                    for role in roles:
                        policies = iam.list_attached_role_policies(RoleName=role['RoleName'])['AttachedPolicies']
                        for policy in policies:
                              # Check if the SSM policy is attached to the role
                            if 'AmazonSSMManagedInstanceCore' in policy['PolicyName']:
                                print(f"Detaching SSM policy from role: {role['RoleName']} in instance: {instance['InstanceId']}")
                                iam.detach_role_policy(
                                    RoleName=role['RoleName'],
                                    PolicyArn=policy['PolicyArn']
                                )
    except ClientError as e:
        print(f"Error processing EC2 instances: {e}")

if __name__ == "__main__":
    remove_ssm_policy_from_ec2_instances()
