from lambda_handler import lambda_handler

event = {
    "query": "apple"
}

response = lambda_handler(event, None)
print(response)
