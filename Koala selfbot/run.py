import discord
import os
from discord.ext import commands

client=commands.Bot(command_prefix=':', self_bot=True, help_command=None, status=discord.Status.idle, intents=discord.Intents.all())

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="Koala Selfbot v1", url="https://twitch.tv/InfamousKoala"))
    os.system('clear')
    print(f'Logged in as {client.user} ({client.user.id})')

client.run("TOKEN", bot=False)
