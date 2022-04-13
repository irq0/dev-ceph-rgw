#!/usr/bin/env python3

import logging
import boto3
from pprint import pprint
from botocore.exceptions import ClientError


s3 = boto3.client('s3',
                  endpoint_url="http://localhost:7480",
                  aws_access_key_id="test",
                  aws_secret_access_key="test")

print("list_buckets:")
pprint(s3.list_buckets())
print("list 'testbucket':")
pprint(s3.list_objects_v2(Bucket="testbucket"))
print("get_object testbucket/testobject:")
obj = s3.get_object(Bucket="testbucket",
                    Key="testobject")
pprint(obj)
pprint(obj['Body'].read())
