
def handle(event, context = {}):
    print(event)
    return {
        'statusCode': 200,
        'body': 'Hello World!',
    }