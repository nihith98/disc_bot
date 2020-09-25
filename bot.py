import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_NAME')
bot = commands.Bot(command_prefix='bb')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
    print(guild.name)
    print(guild.id)

    members = '\n'.join([member.name for member in guild.members])
    print(members)

@bot.event
async def on_member_join(member):
    str = 'Welcome to the Bilal OG '+member.name
    member.create_dm()
    member.dm_channel.send(str)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return 
    if message.content.lower() == 'no u':
        await message.channel.send('no u')
    elif 'cancer' in message.content.lower():
        user = message.author
        resp = 'Cancer ah pannadha da <@'+str(user.id)+'>'
        await message.channel.send(resp)
    elif message.content == 'raise-exception':
        await message.channel.send('Exception acknowledged')
        raise discord.DiscordException


@bot.event
async def on_error(event, *args, **kwargs):
    print(1)
    with open('E:\Hobby_Project\Disc_Bots\Bilal\err.log', 'a') as f:
        print(2)
        if event == 'on_message':
            print(3)
            f.write(f'Unhandled message: {args[0]}\n \n')
        else:
            print(4)
            raise

bot.run(TOKEN)