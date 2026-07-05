import json

def lambda_handler(event, context):

    body = json.loads(event.get("body", "{}"))
    message = body.get("message", "")

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "OPTIONS,POST"
        },
        "body": json.dumps({
            "reply": f"AWS says: {message}"
        })
    }
