import unittest
from unittest.mock import patch, MagicMock
from aws_scripts.scripts.check_rds_public_access import remove_public_access_from_rds_instances

class TestRemovePublicAccessFromRdsInstances(unittest.TestCase):

    @patch('boto3.client')
    def test_remove_public_access_from_rds_instances(self, mock_boto_client):
        mock_rds = MagicMock()
        mock_boto_client.return_value = mock_rds
        
        mock_rds.describe_db_instances.return_value = {
            'DBInstances': [{
                'DBInstanceIdentifier': 'test-instance',
                'PubliclyAccessible': True
            }]
        }
        
        
        remove_public_access_from_rds_instances()
        
        mock_rds.modify_db_instance.assert_called_with(
            DBInstanceIdentifier='test-instance',
            PubliclyAccessible=False,
            ApplyImmediately=True
        )

if __name__ == '__main__':
    unittest.main()
