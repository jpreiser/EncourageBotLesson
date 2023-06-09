import discord
import os
import requests
import json

client = discord.Client(intents=discord.Intents.all())

def Convert(lst):
    it = iter(lst)
    res_dct = dict(zip(it, it))
    return res_dct

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

  if message.content.startswith('/hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('$quote'):
    quote = json.loads(get_quote())
    text = quote[0]
    await message.channel.send(text['quote'] + "\n-" + text['author'])

client.run(os.getenv('TOKEN'))