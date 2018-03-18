import requests, json


def getValues(platform, userName):
    headers = {'TRN-Api-Key' : 'b0c014b6-1210-48bb-8452-c63e9caf00ba'}
    r = requests.get('https://api.fortnitetracker.com/v1/profile/' + platform + '/' + userName, headers=headers)
    parsedJson =  json.dumps(r.json(), ensure_ascii = False)
    loadedJson = json.loads(parsedJson)
    userName = loadedJson['epicUserHandle']
    platformName = loadedJson['platformNameLong']
    print("Platform: " + platformName + "\nUser Name: " + userName)

getValues('pc', 'emilews')