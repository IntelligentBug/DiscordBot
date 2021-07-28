# Imports
import discord
from discord.ext import commands

# Global Variables
Prefix = "."
Token = "pest-your-token-here-and-don't-shere-your-token-with-anyone"

# Making the Main Bot
YoungBug = commands.Bot(command_prefix=Prefix)

# Adding a Event To it
@BlueBug.event
async def on_ready():
# Changing The Presence Of Bot
    await YoungBug.change_presence(activity=discord.Game("Hello There"))
    print('Done!')

# Making The Bot Alive
YoungBug.run(Token)
