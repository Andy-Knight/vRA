Dependency Modules
import requests

#Native Modules
import json
import base64

def getCMDBBlobSha(context, inputs):
	baseUrl = "https://api.github.com"
	repoString = "/repos/Andy-Knight/CS360-vRA/contents/CMDB/" + inputs["resourceNames"][0]

	header = {"Authorization": "Bearer INSERT_BEARER_TOKEN_HERE",
		"Content-Type": "application/json",
		"Accept": "application/vnd.github.v3+json"
		}

	#Execute GET request to GitHub
	response = requests.get(baseUrl + repoString, headers=header)
	print("GitHub response code is: " + str(response.status_code))

	sha = json.loads(response.text)['sha']
	print("File SHA is: " + str(sha))

	outputs = {}
	outputs['recordSha'] = str(sha)
	return outputs
