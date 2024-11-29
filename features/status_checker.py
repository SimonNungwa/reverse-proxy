import httpx

class handleRequest:
    def __init__(self, site):
        self.site = site
        # self.addr = addr
        # self.port = port


    # return status code for a site
    def checkStatus(self):
        try:
            response = httpx.get(self.site)
            return response.status_code
        except httpx.RequestError as e:
            return f'an error occured: {e}'

print('Enter the site URL')
site = input().strip()
requestHandler = handleRequest(site)
result = requestHandler.checkStatus()

print(result)
