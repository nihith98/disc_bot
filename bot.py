##Generic Imports
from os import environ
from decouple import config ##requirements.txt

##Discord Imports
import discord ##requirements.txt
import youtube_dl ##requirements.txt
from discord.ext import commands

#Bilal Imports
import noobhi
import vathsa

##BilalUtil Imports
import bilalUtil as bu
import isUser as iu

TOKEN = environ.get('DISCORD_TOKEN')
GUILD = environ.get('GUILD_NAME')
bot = commands.Bot(command_prefix='bb')


@bot.event
async def on_ready():
    print(f'{bot.user.name} Bot has connected to Discord!')
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
    
    user = message.author
    client = discord.Client()

    ##Prevents infinite loop
    if message.author == bot.user:
        return 
    
    ##No u max 
    if message.content.lower() == 'no u': 
        await message.channel.send('no u')
    
    ## Cancer ah Pannadha da @User
    elif 'cancer' in message.content.lower():
        
        resp = 'Cancer ah pannadha da <@'+str(user.id)+'>'
        print(str(user.id))
        await message.channel.send(resp)

    ##Praise Noobhi with random title 
    elif message.content.lower() == 'praise noobhi':
        t = noobhi.random_title()
        await message.channel.send(t)
        for member in guild.members:
            print(member.name)
            if iu.isNoobhi(member.name):
                print("4")
                await member.edit(nick=t)
                print(member.nick)

    ##Rain Money when vathsa types
    elif iu.isVathsa(user.name):
        text = vathsa.rainMoney()
        await message.channel.send(text)

    ##Exception and Logging test
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
            
@bot.command(name="anthem")
async def bilalAnthem(ctx):
    # Gets voice channel of message author
    voice_channel = ctx.author.channel
    channel = None
    if voice_channel != None:
        channel = voice_channel.name
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio('/app/Alarm.mp3'))
        # Sleep while audio is playing.
        while vc.is_playing():
            sleep(.1)
        await vc.disconnect()
    else:
        await ctx.send(str(ctx.author.name) + "is not in a channel.")

bot.run(TOKEN)