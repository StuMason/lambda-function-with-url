# HTTP Endpoint for Single Lambda Function

Function with exposed HTTPS endpoint created automatically by AWS Lambda.

```yaml
  WebhookFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: handler.handle
      Runtime: python3.9
      Description: Cheeky Webhook
      FunctionUrlConfig:
        AuthType: NONE
```

## Event dict

```python
{
  'version': '2.0', 
  'routeKey': 
  '$default', 
  'rawPath': '/', 
  'rawQueryString': '', 
  'headers': {
    'sec-fetch-mode': 'navigate', 
    'sec-fetch-site': 'cross-site', 
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8', 
    'x-forwarded-proto': 'https', 
    'x-forwarded-port': '443', 
    'x-forwarded-for': '127.0.0.1', 
    'sec-fetch-user': '?1', 
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"', 
     'sec-ch-ua-mobile': '?0', 
     'x-amzn-trace-id': 'Root=1-624eb061-7cfa4cfc118fab7207f9540d', 
     'sec-ch-ua-platform': '"macOS"', 
     'host': 'domain_id.lambda-url.eu-west-1.on.aws', 
     'upgrade-insecure-requests': '1', 
     'accept-encoding': 'gzip, deflate, br', 
     'sec-fetch-dest': 'document', 
     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}, 
     'requestContext': {
       'accountId': 'anonymous', 
       'apiId': 'domain_id', 
       'domainName': 'domain_id.lambda-url.eu-west-1.on.aws', 
       'domainPrefix': 'domain_id', 
       'http': {
         'method': 'GET', 
         'path': '/', 
         'protocol': 'HTTP/1.1', 
         'sourceIp': '127.0.0.1',
        'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'
      }, 
    'requestId': 'b704195f-eaaf-4ac1-9123-0e57c41aef41', 
    'routeKey': '$default', 
    'stage': '$default', 
    'time': '07/Apr/2022:09:35:30 +0000', 
    'timeEpoch': 1649324130016
  }, 
  'isBase64Encoded': False
}
```
