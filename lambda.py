import json
import boto3

def lambda_handler(event, context):
    sesClient = boto3.client("ses" , region_name="us-east-1")
    
    emailResponse = sesClient.send_email(  
    Destination = {
        "ToAddresses" : [
            "hunnybagla@gmail.com"
        ],
    },
    Message = {
        "Body": {
            "Text": {
                "Data" :  "This is my first email through SES and Lambda"
            }
        },
    
        "Subject" : {
            "Data": "think of any good subject"
        },
    },
    Source = "hunnybagla@gmail.com"
    )
