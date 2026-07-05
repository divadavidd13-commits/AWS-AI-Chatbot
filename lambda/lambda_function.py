import json
import os
import urllib.request

API_KEY = os.environ["GEMINI_API_KEY"]

def lambda_handler(event, context):

    try:
        body = json.loads(event.get("body", "{}"))
        message = body.get("message", "")

        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": message
                        }
                    ]
                }
            ]
        }

        req = urllib.request.Request(
            f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json"
            },
            method="POST"
        )

        with urllib.request.urlopen(req) as response:

            result = json.loads(response.read().decode())

            print(result)

            reply = result["candidates"][0]["content"]["parts"][0]["text"]

            return {
                "statusCode": 200,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Headers": "Content-Type",
                    "Access-Control-Allow-Methods": "OPTIONS,POST"
                },
                "body": json.dumps({
                    "reply": reply
                })
            }

    except Exception as e:

        print("ERROR:", str(e))

        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            "body": json.dumps({
                "error": str(e)
            })
        }
