import json
import os
def lambda_handler(event, context):
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda in '+ os.environ.get('Env'))
    }