#Dependency Modules
import requests

#Native Modules
import json
import base64

def getCMDBRecord(context, inputs):
	baseUrl = "https://api.github.com"
	repoString = "/repos/Andy-Knight/CS360-vRA/contents/CMDB/" + inputs["resourceNames"][0]

	header = {"Authorization": "Bearer INSERT_BEARER_TOKEN_HERE",
		"Content-Type": "application/json",
		"Accept": "application/vnd.github.v3+json"
		}

	#Execute GET request to GitHub
	response = requests.get(baseUrl + repoString, headers=header)
	print("GitHub response code is: " + str(response.status_code))

	base64EncodedContent = json.loads(response.text)['content']
	decodeContent = base64.b64decode(base64EncodedContent)
	finalContentString = decodeContent.decode('ascii')
	print("File contents string is: " + finalContentString)
	noNewLine = json.dumps(finalContentString).replace('\\n', '')
	noSpaces = noNewLine.replace(' ', '')
	print(noSpaces)

	outputs = {}
	outputs['cmdbRecordString'] = noSpaces

	return outputs
