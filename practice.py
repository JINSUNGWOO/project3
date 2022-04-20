import requests
import json


url = "https://api-football-beta.p.rapidapi.com/teams/statistics"

querystring = {'team':'49',"season":"2021","league":"39"} # team:33 [MU] 38[Watford]

headers = {
	"X-RapidAPI-Host": "api-football-beta.p.rapidapi.com",
	"X-RapidAPI-Key": "5562bffd9bmshb429d3a70bc84e4p1606fcjsn54ebc11d9651"
}

response = requests.request("GET", url, headers=headers, params=querystring)

content = response.text # str
json_obj = json.loads(content) # dict
json_dump = json.dumps(content) # str
print(json_obj['response']['team']['name'])
print(json_obj['response'])