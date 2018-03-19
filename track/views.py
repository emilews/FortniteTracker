import json
import requests
from django.shortcuts import render


def home(request):
    return render(request, 'track/index.html')


def graphs(request):
    username = 'emilews'
    platform = 'pc'
    headers = {'TRN-Api-Key': 'b0c014b6-1210-48bb-8452-c63e9caf00ba'}
    r = requests.get('https://api.fortnitetracker.com/v1/profile/' + platform + '/' + username, headers = headers)
    parsedJson = json.dumps(r.json(), ensure_ascii=False)
    loadedJson = json.loads(parsedJson)
    epicHandle = loadedJson['epicUserHandle']
    platformName = loadedJson['platformNameLong']
    stats = loadedJson['lifeTimeStats']
    totalScore = stats[6]['value']
    totalMatches = stats[7]['value']
    totalWins = stats[8]['value']
    winsPercentage = stats[9]['value']
    totalKills = stats[10]['value']
    kdRatio = stats[11]['value']
    killsPerMinute = stats[12]['value']
    totalPlayedTime = stats[13]['value']
    averageTimeSurvival = stats[14]['value']
    dataDict = dict(userName=epicHandle, platform=platformName, totalScore=totalScore, totalMatches=totalMatches,
                    totalWins=totalWins, winsPercentage=winsPercentage, totalKills=totalKills, kdRatio=kdRatio,
                    killsPerMinute=killsPerMinute, totalPlayedTime=totalPlayedTime,
                    averageTimeSurvival=averageTimeSurvival)

    return render(request, 'track/graphs.html', dataDict)


