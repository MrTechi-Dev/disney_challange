import unittest
from unittest.mock import patch, MagicMock
from aws_scripts.scripts.check_ec2_ssm_policy import remove_ssm_policy_from_ec2_instances

class TestRemoveSsmPolicyFromEc2Instances(unittest.TestCase):

    @patch('boto3.client')
    def test_remove_ssm_poalicy_from_ec2_instances(self, mock_boto_client):
        mock_ec2 = MagicMock()
        mock_iam = MagicMock()
        mock_boto_client.side_effect = [mock_ec2, mock_iam]
        
        mock_ec2.describe_instances.return_value = {
            'Reservations': [{
                'Instances': [{
                    'InstanceId': 'i-1234567890abcdef0',
                    'IamInstanceProfile': {'Arn': 'arn:aws:iam::123456789012:instance-profile/test-profile'}
                }]
            }]
        }
        
        mock_iam.get_instance_profile.return_value = {
            'InstanceProfile': {
                'Roles': [{'RoleName': 'test-role'}]
            }
        }
        
        mock_iam.list_attached_role_policies.return_value = {
            'AttachedPolicies': [{
                'PolicyName': 'AmazonSSMManagedInstanceCore',
                'PolicyArn': 'arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore'
            }]
        }
        
        
        remove_ssm_policy_from_ec2_instances()
        
        mock_iam.detach_role_policy.assert_called_with(
            RoleName='test-role',
            PolicyArn='arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore'
        )

if __name__ == '__main__':
    unittest.main()
