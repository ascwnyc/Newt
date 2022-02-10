from discord.ext import commands
import discord
import datetime

# import
from config import *

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # !unload cogs.<cog_name> // Unload cog function
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, cog: str):
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send('Could not unload cog')
            return
        await ctx.send('Cog unloaded')

    # !load cogs.<cog_name> // Load cog function
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, cog: str):
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send('Could not load cog')
            return
        await ctx.send('Cog loaded')

    # !reload cogs.<cog_name> // Cog reload function
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, cog: str):
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send('Could not reload cog')
            return
        await ctx.send('Cog reloaded')

    # !status // Server information function
    @commands.command()
    #@commands.has_permissions(administrator=True)
    async def server(self, ctx, *args):
        # shorthand guild var
        guild = ctx.guild

        # fetch # of text/voice channels var    
        no_voice_channels = len(guild.voice_channels)
        no_text_channels = len(guild.text_channels)

        # create embed
        embed = discord.Embed(title='Server Information')#, colour=bot_colour)
        
        embed.set_author(name='Newt', url=bot_url, icon_url=bot_avatar)

        embed.add_field(name='Server Name', value=guild.name, inline=False)

        # custom emotes field
        emote_string = ''
        for e in guild.emojis:
            if e.is_usable():
                emote_string += str(e)
        embed.add_field(name='Custom Emotes', value=emote_string or 'No emotes available', inline=False)

        # text/voice channel quantity field
        embed.add_field(name='Voice Channels', value=no_voice_channels)
        embed.add_field(name='Text Channels', value=no_text_channels)

        # server icon as thumbnail field
        embed.set_thumbnail(url=guild.icon_url)
        
        embed.add_field(name='AFK Channel', value=guild.afk_channel, inline=False)

        # footer field // dependencies: datetime
        embed.set_footer(text=datetime.datetime.now())
        
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Admin(bot))
