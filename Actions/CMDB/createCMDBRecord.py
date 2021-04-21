#Dependency Modules
import requests

#Native Modules
import json
import base64

def createCMDBRecord(context, inputs):
	baseUrl = "https://api.github.com"
	repoString = "/repos/Andy-Knight/CS360-vRA/contents/CMDB/" + inputs["resourceNames"][0]

	header = {"Authorization": "Bearer 11da7c4785f4d0953377eb06d1a7a3e23ef8c796",
		"Content-Type": "application/json",
		"Accept": "application/vnd.github.v3+json"
		}
	
	#Build content for record
	messageContent = {"Hostname": inputs['resourceNames'][0],
		"deploymentId": inputs['deploymentId'],
		"deploymentImage": inputs['customProperties']['image'],
		"buildState": "Provisioning"
		}
	messageString = json.dumps(messageContent, sort_keys=True, indent=4)

	#Convert content into base64 (required by Github)
	contentInBytes = messageString.encode('ascii')
	bytesToBase64 = base64.b64encode(contentInBytes)
	base64Content = bytesToBase64.decode('ascii')
	print("Encoded base64 content is: " + base64Content)

	#Build message body for request
	body = {"message": "CMDB Record", "content": base64Content}

	#Execute PUT request to GitHub
	response = requests.put(baseUrl + repoString, headers=header, data=json.dumps(body))
	print("GitHub response code is: " + str(response.status_code))
