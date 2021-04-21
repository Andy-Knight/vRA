import requests
import json
from requests.auth import HTTPBasicAuth

def handler(context, inputs):
    #Define variables with values
    requestUrl = "https://vcsa-01a.corp.local/rest/com/vmware/cis/session"
    auth = "Basic YWRtaW5pc3RyYXRvckB2c3BoZXJlLmxvY2FsOlZNd2FyZTEh"
    headers = {"Content-Type": "application/json", "Accept": "application/json", "Authorization": auth}
    
    #Execute POST request using variables
    response = requests.post(requestUrl, headers = headers, verify = False)
    print('Request response code is: ' + str(response.status_code))
    
    #Extract response body as JSON using inbuilt json() method
    jsonResponse = response.json()
    print('VC API token is: ' + jsonResponse.get('value'))
    
    #Create output dictionary with return keys and values
    outputs = {}
    outputs['apiToken'] = jsonResponse.get('value')
    return outputs
