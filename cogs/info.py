from discord.ext import commands
import discord

# import
from config import bot_url, bot_colour

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):

        embed = discord.Embed(
        
        colour = bot_colour,
        
        # title='Newt', 
        
        description='''I'm a multi-purpose discord bot designed for niche servers. 
        Heres a list of commands.
        
        Input `/help <command>` for extended information on a command.
        
        **Tip/** You can view all commands at: [newt.io](https://ascwnyc.github.io/Newt)'''
        
        )

        embed.add_field(name=':red_circle: Reddit', value='`/reddit`', inline=False)
        embed.add_field(name=':hammer: Admin', value='`/kick`, `/ban`, `/unban`', inline=False)
        embed.add_field(name=':wrench: Settings', value='`/load`, `/unload`, `/reload`', inline=False)
        embed.add_field(name=':information_source: Information', value='`/help`, `/server`', inline=False)
        
        embed.set_author(name='Newt', url=bot_url, icon_url=self.bot.user.avatar_url)
    
        await ctx.send(embed=embed)

### /// REDDIT

    # /help <reddit> // Shows this command's usage.
    @help.command()
    async def reddit(self, ctx):

        embed = discord.Embed(
        
        colour = bot_colour,
        
        title='/reddit', 
        
        description='''Pulls a random post from [reddit](https://reddit.com). A range of subreddits are supported.
        
        Examples:
        `/reddit funny` - Pulls a post from the subreddit 'funny'.
        `/reddit funny top` - Pulls a post, from the subreddit 'funny' and sorts the posts to pull from by 'top'.'''
        
        )

        embed.add_field(name='Usage', value='`/reddit <subreddit>`\n`/reddit <subreddit> [category]`', inline=True)
        embed.add_field(name='Permissions', value='`none`', inline=True)
    
        embed.set_author(name='Newt', url=bot_url, icon_url=self.bot.user.avatar_url)
    
        await ctx.send(embed=embed)
        
### /// ADMIN

    # /help <kick> // Shows this command's usage.
    @help.command()
    async def kick(self, ctx):

        embed = discord.Embed(
        
        colour = bot_colour,
        
        title='/kick', 
        
        description='''Kicks a user from your server.'''
        
        )

        embed.add_field(name='Usage', value='`/kick <user>`', inline=True)
        embed.add_field(name='Permissions', value='`kick_members`', inline=True)
    
        embed.set_author(name='Newt', url=bot_url, icon_url=self.bot.user.avatar_url)
    
        await ctx.send(embed=embed)

    # /help <ban> // Shows this command's usage.
    @help.command()
    async def ban(self, ctx):

        embed = discord.Embed(
        
        colour = bot_colour,
        
        title='/ban', 
        
        description='''Bans a user from your server. You can optionally provide a reason for the ban.'''
        
        )

        embed.add_field(name='Usage', value='`/ban <user>`\n`/ban <user> [reason]`', inline=True)
        embed.add_field(name='Permissions', value='`ban_members`', inline=True)
    
        embed.set_author(name='Newt', url=bot_url, icon_url=self.bot.user.avatar_url)
    
        await ctx.send(embed=embed)

    # /help <unban> // Shows this command's usage.
    @help.command()
    async def unban(self, ctx):

        embed = discord.Embed(
        
        colour = bot_colour,
        
        title='/unban', 
        
        description='''Unbans a user from your server.'''
        
        )

        embed.add_field(name='Usage', value='`/unban <user>`', inline=True)
        embed.add_field(name='Permissions', value='`ban_members`', inline=True)
    
        embed.set_author(name='Newt', url=bot_url, icon_url=self.bot.user.avatar_url)
    
        await ctx.send(embed=embed)

### /// SETTINGS

    # /help <load> // Shows this command's usage.
    @help.command()
    async def load(self, ctx):

        embed = discord.Embed(
        
        colour = bot_colour,
        
        title='/load', 
        
        description='''Loads a cog for use.'''
        
        )

        embed.add_field(name='Usage', value='`/load cogs.<cog>`', inline=True)
        embed.add_field(name='Permissions', value='`administrator`', inline=True)
    
        embed.set_author(name='Newt', url=bot_url, icon_url=self.bot.user.avatar_url)
    
        await ctx.send(embed=embed)

    # /help <unload> // Shows this command's usage.
    @help.command()
    async def unload(self, ctx):

        embed = discord.Embed(
        
        colour = bot_colour,
        
        title='/unload', 
        
        description='''Unloads a cog from use.'''
        
        )

        embed.add_field(name='Usage', value='`/unload cogs.<cog>`', inline=True)
        embed.add_field(name='Permissions', value='`administrator`', inline=True)
    
        embed.set_author(name='Newt', url=bot_url, icon_url=self.bot.user.avatar_url)
    
        await ctx.send(embed=embed)

    # /help <reload> // Shows this command's usage.
    @help.command()
    async def reload(self, ctx):

        embed = discord.Embed(
        
        colour = bot_colour,
        
        title='/reload', 
        
        description='''Reloads a cog by unloading and loading a cog simeltaneously.'''
        
        )

        embed.add_field(name='Usage', value='`/reload cogs.<cog>`', inline=True)
        embed.add_field(name='Permissions', value='`administrator`', inline=True)
    
        embed.set_author(name='Newt', url=bot_url, icon_url=self.bot.user.avatar_url)
    
        await ctx.send(embed=embed)

### /// INFORMATION

    # /help <server> // Shows this command's usage.
    @help.command()
    async def server(self, ctx):

        embed = discord.Embed(
        
        colour = bot_colour,
        
        title='/server', 
        
        description='''Returns a report of general server information.'''
        
        )

        embed.add_field(name='Usage', value='`/server`', inline=True)
        embed.add_field(name='Permissions', value='`none`', inline=True)
    
        embed.set_author(name='Newt', url=bot_url, icon_url=self.bot.user.avatar_url)
    
        await ctx.send(embed=embed)

def setup(bot):
     bot.add_cog(Info(bot))