import requests
import json

pointsKey = 'points'
url = 'https://memeservice.cfapps.io/api/memes'

def filterMemes( memes ):
  filteredMemes = [ meme for meme in memes if meme[pointsKey] > 60000]
  return filteredMemes

def sumMemes( memes ):
  sumOfPoints = sum( meme[pointsKey] for meme in memes )
  return sumOfPoints

def minimumPoints( memes ):
  sortedMemes = sorted(memes, key = lambda meme: meme[pointsKey])
  return sortedMemes[0][pointsKey]

response = requests.get(url)
memeArray = json.loads(response.text)

print("All memes with more than 60,000 points")
print(json.dumps(filterMemes(memeArray)))
print("Sum of meme points: " + str(sumMemes(memeArray)))
print("Min points: " + str(minimumPoints(memeArray)))
