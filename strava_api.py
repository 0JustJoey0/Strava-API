import urllib3
import requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"

payload = {
    'client_id': "67453",
    'client_secret': '57255eea0a51c2d2f1651dcccd08935aece2e4fd',
    'refresh_token': '09ca5e64cf802283db97e5cc9a26915f32e66241',
    'grant_type': "refresh_token",
    'f': 'json'
}

print("Requesting Token...\n")
res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()['access_token']
print("Access Token = {}\n".format(access_token))

header = {'Authorization': 'Bearer ' + access_token}
param = {'per_page': 200, 'page': 1}
my_dataset = requests.get(activites_url, headers=header, params=param).json()

fh = open("strava.csv", "w")

for item in my_dataset:
    date = item["start_date"]
    name = item["name"]
    distance = item["distance"]
    moving = item["moving_time"]
    fh.write("{},{},{:.2f},{:.2f}\n".format(date[0:10], name, distance/1000, moving/60))

fh.close()
