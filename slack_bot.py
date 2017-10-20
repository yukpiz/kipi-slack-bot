# -*- coding: utf-8 -*-

import json

def lambda_handler(event, context):
    print("-------------------------------")
    print(event)
    print("-------------------------------")
    payload = {
        "text": "hi?"
    }
    return { "statusCode": 200, "body": json.dumps(payload) }