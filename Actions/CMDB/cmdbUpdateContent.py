Dependency Modules
import requests

#Native Modules
import json
import base64

def cmdbUpdateContent(context, inputs):
	cmdbRecord = inputs['cmdbRecordString']
	cmdbRecordStrip = cmdbRecord.replace('\\','')
	cmdbRecordStrip = cmdbRecordStrip.strip('\"')

	recordDict = json.loads(cmdbRecordStrip)
	recordDict['buildState'] = 'Provisioned'
	recordDict['IP'] = inputs['addresses'][0][0]
	print("Changing state and adding IP address to record string")

	baseUrl = "https://api.github.com"
	repoString = "/repos/Andy-Knight/CS360-vRA/contents/CMDB/" + inputs["resourceNames"][0]

	header = {"Authorization": "Bearer INSERT_BEARER_TOKEN_HERE",
		"Content-Type": "application/json",
		"Accept": "application/vnd.github.v3+json"
		}

	messageString = json.dumps(recordDict, sort_keys=True, indent=4)

	#Convert content into base64 (required by Github)
	contentInBytes = messageString.encode('ascii')
	bytesToBase64 = base64.b64encode(contentInBytes)
	base64Content = bytesToBase64.decode('ascii')
	print("Encoded base64 content is: " + base64Content)

	#Build message body for request
	body = {"message": "CMDB Record", "content": base64Content, "sha": inputs['recordSha']}

	#Execute PUT request to GitHub
	response = requests.put(baseUrl + repoString, headers=header, data=json.dumps(body))
	print("GitHub response code is: " + str(response.status_code))
