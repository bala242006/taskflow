import json
import boto3
from datetime import datetime

s3 = boto3.client("s3")
sns = boto3.client("sns")

BUCKET = "YOUR_BUCKET_NAME"
TOPIC_ARN = "YOUR_SNS_TOPIC_ARN"

def lambda_handler(event, context):
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%S")

    alert = {
        "timestamp": timestamp,
        "event": event
    }

    key = f"alerts/cpu-alert-{timestamp}.json"

    s3.put_object(
        Bucket=BUCKET,
        Key=key,
        Body=json.dumps(alert)
    )

    sns.publish(
        TopicArn=TOPIC_ARN,
        Subject="TaskFlow CPU Alert",
        Message=json.dumps(alert, indent=2)
    )

    return {
        "statusCode": 200,
        "body": "Alert processed successfully"
    }
