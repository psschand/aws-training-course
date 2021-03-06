import base64
import logging
import urllib.parse
import uuid

import boto3

L = logging.getLogger(__name__)
L.setLevel(logging.DEBUG)

s3_client = boto3.client('s3')


def lambda_handler(event, context):
    bucket = 'zj001-photo'
    key = urllib.parse.unquote_plus(event['imageKey'])
    content = base64.b64decode(event['image'])

    upload_path = '/tmp/{}{}'.format(uuid.uuid4(), key)

    with open(upload_path, 'wb') as outf:
        outf.write(content)
    L.info('going to upload %s to %s/%s', upload_path, bucket, key)

    s3_client.upload_file(upload_path, bucket, key)
