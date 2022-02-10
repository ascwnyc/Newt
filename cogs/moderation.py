import discord
from discord.ext import commands

# import
from config import *

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # !kick <user> // Kick user function
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, reason: str = 'N/A'):
        if member is not None:
            await ctx.guild.kick(member, reason=reason)
            embed = discord.Embed(
        
            colour = bot_colour,
        
            title='', 
        
            description=f'{member} was kicked for {reason}.'
        
            )
    
            embed.set_author(name="Newt", url=bot_url, icon_url=self.bot.user.avatar_url)
    
            await ctx.send(embed=embed)           
        else:
            embed = discord.Embed(
        
            colour = bot_colour,
        
            title='', 
        
            description='Use `@mention` to highlight who you would like to kick.'
        
            )
    
            embed.set_author(name="Newt", url=bot_url, icon_url=self.bot.user.avatar_url)
    
            await ctx.send(embed=embed) 

    # !ban <user> // Ban user function
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, reason: str = 'N/A'):
        if member is not None:
            await ctx.guild.ban(member, reason=reason)
            embed = discord.Embed(
        
            colour = bot_colour,
        
            title='', 
        
            description=f'{member} was banned for {reason}.'
        
            )
    
            embed.set_author(name="Newt", url=bot_url, icon_url=self.bot.user.avatar_url)
    
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
        
            colour = bot_colour,
        
            title='', 
        
            description='Use `@mention` to highlight who you would like to ban.'
        
            )
    
            embed.set_author(name="Newt", url=bot_url, icon_url=self.bot.user.avatar_url)
    
            await ctx.send(embed=embed)

    # !unban <user> // Ban user function
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member: str = '', reason: str = 'Reason'):
        if member == '':
            embed = discord.Embed(
        
            colour = bot_colour,
        
            title='', 
        
            description='Error in unbanning process. Use plain text when referring to the user you wish to unban.'
        
            )
    
            embed.set_author(name="Newt", url=bot_url, icon_url=self.bot.user.avatar_url)
    
            await ctx.send(embed=embed)
            return

        bans = await ctx.guild.bans()
        for b in bans:
            if b.user.name == member:
                await ctx.guild.unban(b.user, reason=reason)
                embed = discord.Embed(
        
                colour = bot_colour,
        
                title='', 
        
                description=f'{member} was unbanned.'
        
                )
    
                embed.set_author(name="Newt", url=bot_url, icon_url=self.bot.user.avatar_url)
    
            await ctx.send(embed=embed)
            return
        await ctx.send('User was not found in ban list.')



def setup(bot):
     bot.add_cog(Moderation(bot))