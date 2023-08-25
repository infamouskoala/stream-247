import discord
import os
from discord.ext import commands

client=commands.Bot(command_prefix=':', self_bot=True, help_command=None)

token = input("enter token: ")

@client.event
async def on_ready():
    os.system('clear')
    await client.change_presence(activity=discord.Streaming(name="1337", url="https://twitch.tv/koala_from_mars"))
    print(f'Logged in as {client.user} ({client.user.id})')

client.run(token, bot=False)
