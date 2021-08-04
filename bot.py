import discord
from discord.ext import commands

# Global variables
Token = "Your-Toke-here"
Prefix = "b!"
noob = commands.Bot(command_prefix=Prefix)
badwords = ['bad', 'words', 'here']
CH_ID = "Channel Id here"

# Simple Event
@noob.event
async def on_ready():
    await noob.change_presence(activity=discord.Game("WoW"))
    print('Yeah Boi!')

# moderation command (links remover and Words remover)
@noob.event
async def on_message(message):
    if 'https://' in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} Don't send links to the server")

    for i in badwords:
        if i in message.content:
            await message.delete()
            await message.channel.send(f"{message.author.mention} Don't use this type of language")
            noob.dispatch('profanity', message, i)
            return
        await noob.process_commands(message)

# Logging the words to the channel
@noob.event
async def on_profanity(message, word):
    channel = noob.get_channel(CH_ID)
    emd = discord.Embed(description=f'{message.author.name} Just said || {word} ||', colour=discord.Color.random())
    await channel.send(embed=emd)

# running the bot
noob.run(Token)
