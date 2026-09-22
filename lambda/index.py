import json
import boto3
from datetime import datetime, timezone

s3 = boto3.client("s3")
sns = boto3.client("sns")

BUCKET = "taskflow-alert-logs-78de66aa"
TOPIC_ARN = "arn:aws:sns:ap-south-1:704348946409:taskflow-alerts"


def lambda_handler(event, context):
    print("ALERTMANAGER EVENT:")
    print(json.dumps(event, indent=2))

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%S")

    alert = {
        "timestamp": timestamp,
        "event": event
    }

    key = f"alerts/cpu-alert-{timestamp}.json"

    # Save alert to S3
    s3.put_object(
        Bucket=BUCKET,
        Key=key,
        Body=json.dumps(alert, indent=2)
    )

    # Send email through SNS
    sns.publish(
        TopicArn=TOPIC_ARN,
        Subject="TaskFlow CPU Alert",
        Message=json.dumps(alert, indent=2)
    )

    return {
        "statusCode": 200,
        "body": "CPU alert processed successfully"
    }
