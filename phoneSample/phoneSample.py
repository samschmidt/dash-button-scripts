'''
This is a sample Lambda function that sends an SMS on click of a
button. It needs one permission sns:Publish. The following policy
allows SNS publish to SMS but not topics or endpoints.
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sns:Publish"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Deny",
            "Action": [
                "sns:Publish"
            ],
            "Resource": [
                "arn:aws:sns:*:*:*"
            ]
        }
    ]
}

The following JSON template shows what is sent as the payload:
{
    "serialNumber": "GXXXXXXXXXXXXXXXXX",
    "batteryVoltage": "xxmV",
    "clickType": "SINGLE" | "DOUBLE" | "LONG"
}

A "LONG" clickType is sent if the first press lasts longer than 1.5 seconds.
"SINGLE" and "DOUBLE" clickType payloads are sent for short clicks.

For more documentation, follow the link below.
http://docs.aws.amazon.com/iot/latest/developerguide/iot-lambda-rule.html
'''

from __future__ import print_function

import boto3
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


#phoneAngela = '18596281888'
phoneSam = '18597508490'

sns = boto3.client('sns')
phone_number = phoneSam;

def lambda_handler(event, context):
    logger.info('Received event: ' + json.dumps(event))
    message = 'Henlo from your IoT Button %s. Here is the full event: %s' % (event['serialNumber'], json.dumps(event))
    sns.publish(PhoneNumber=phone_number, Message=message)
    logger.info('SMS has been sent to ' + phone_number)