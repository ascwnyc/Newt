from discord.ext import commands
import discord

# import
from config import bot_url, bot_colour

class Template(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def template(self, ctx):

        # Embedded template
        embed = discord.Embed(
        
        colour = bot_colour,
        
        title='', 
        
        description=''
        
        )
    
        embed.set_author(name="Newt", url=bot_url, icon_url=self.bot.user.avatar_url)
    
        await ctx.send(embed=embed)

def setup(bot):
     bot.add_cog(Template(bot))