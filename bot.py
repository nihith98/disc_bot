import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_NAME')
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(guild.name)
    print(guild.id)

    members = '\n'.join([member.name for member in guild.members])
    print(members)

@client.event
async def on_member_join(member):
    str = 'Welcome to the Bilal OG '+member.name
    await member.create_dm()
    await member.dm_channel.send(str)

@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    if message.content.lower() == 'no u':
        await message.channel.send('no u')
    elif 'cancer' in message.content.lower():
        user = message.author
        resp = 'Cancer ah pannadha da <@'+str(user.id)+'>'
        await message.channel.send(resp)
    


client.run(TOKEN)