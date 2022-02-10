import os
import discord



# // Discord Configuration Settings (TOKEN)
DISCORD_TOKEN = os.environ['DISCORD_TOKEN']

# // Reddit Configuration Settings
REDDIT_APP_ID = os.environ['REDDIT_APP_ID']
REDDIT_APP_TOKEN = os.environ['REDDIT_APP_TOKEN']

# // Bot Strings
# bot_avatar = "https://i.imgur.com/ayk78Kg.png" # deprecated, uses 'self.bot.user.avatar_url' instead.
bot_url = "https://ascwnyc.github.io/Newt/"
bot_colour = discord.Colour.dark_theme()
color_reddit = 0xFF3F18