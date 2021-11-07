import requests

url = "https://dadjokegenerator.com"

payload={}
headers = {
       'Accept': 'application/json'
	
respone = requests.request("Get", url, headers=headers, data=payload)
	
print (response.text)
	
	
	
