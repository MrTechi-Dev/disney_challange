import unittest
from unittest.mock import patch, MagicMock
import boto3
from aws_scripts.scripts.check_s3_public_access import remove_public_access_from_s3_buckets

class TestRemovePublicAccessFromS3Buckets(unittest.TestCase):

    @patch('boto3.client')
    def test_remove_public_access_from_s3_buckets(self, mock_boto_client):
        mock_s3 = MagicMock()
        mock_boto_client.return_value = mock_s3
        
        mock_s3.list_buckets.return_value = {
            'Buckets': [{'Name': 'test-bucket'}]
        }
        
        mock_s3.get_bucket_acl.return_value = {
            'Grants': [{
                'Grantee': {'Type': 'Group', 'URI': 'http://acs.amazonaws.com/groups/global/AllUsers'}
            }]
        }
        
       
        remove_public_access_from_s3_buckets()
        
        mock_s3.put_bucket_acl.assert_called_with(Bucket='test-bucket', ACL='private')

if __name__ == '__main__':
    unittest.main()
