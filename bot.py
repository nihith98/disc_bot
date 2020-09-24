import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('NzU4NjA3MDAzMDkzOTU4Njc3.X2xZ0w.H_tzdYtAiZYA953kev-qFT1wE9k')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run('NzU4NjA3MDAzMDkzOTU4Njc3.X2xZ0w.H_tzdYtAiZYA953kev-qFT1wE9k')