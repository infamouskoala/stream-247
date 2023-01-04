import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client=commands.Bot(command_prefix=':', self_bot=True, help_command=None)

x = input("enter token: ")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="1337", url="https://twitch.tv/infamouskoala"))
    os.system('clear')
    print("Logged in")

client.run(x, bot=False)
