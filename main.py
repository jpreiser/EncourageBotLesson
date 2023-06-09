import discord
import os
import requests
import json
import random

client = discord.Client(intents=discord.Intents.all())

sad_words = ["sad", "depressed", "unhappy", "uninspired", "depressing"]

starter_encouragements = [
  "Cheer up!", 
  "Hang in there!", 
  "You got this, don't give up!", 
  "https://www.youtube.com/watch?v=KxGRhd_iWuE"
]

def get_quote():
  category = ''
  api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
  response = requests.get(api_url, headers={'X-Api-Key': os.getenv('API_NINJA_KEY')})
  if response.status_code == requests.codes.ok:
    return(response.text)  
  else:
    return("Error: ", response.status_code, response.text)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  
  if msg.startswith('/hello'):
    await message.channel.send('Hello!')

  if msg.startswith('/quote'):
    quote = json.loads(get_quote())
    text = quote[0]
    await message.channel.send(text['quote'] + "\n-" + text['author'])

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

client.run(os.getenv('TOKEN'))