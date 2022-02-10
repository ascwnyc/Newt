import discord
import os
from discord.ext import commands

# import
from config import DISCORD_TOKEN

bot = commands.Bot(command_prefix="/")
bot.remove_command("help")

# // On_Ready() Events
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!') # Bot online console confirmation
    await bot.change_presence(activity=discord.Game(name=f'/help | {len(bot.guilds)} servers'))

# // Load all Cogs ('root/cogs/...')
for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(DISCORD_TOKEN)