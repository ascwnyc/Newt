from discord.ext import commands
import asyncpraw
import random
import discord

# import
from config import REDDIT_APP_ID, REDDIT_APP_TOKEN, color_reddit

all_subs = []

class Reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = asyncpraw.Reddit(client_id=REDDIT_APP_ID, client_secret=REDDIT_APP_TOKEN, user_agent="Newt", )

    @commands.command(description='''Pulls a random post from [reddit](https://reddit.com). A range of subreddits are supported. 
    
    Examples:
    `!reddit funny` - Pulls a post from the subreddit 'funny'.
    `!reddit funny top` - Pulls a post, from the subreddit 'funny' and sorts the posts to pull from by 'top'.''')
    
    async def reddit(self, ctx, sub='help'):
        subreddit = await self.reddit.subreddit(sub)

        #top = subreddit.top(limit = 10)
        
        async for submission in subreddit.top(limit=20):
            all_subs.append(submission)
        
        print('sorted by top...')
        random_sub = random.choice(all_subs)

        embed = discord.Embed(title=random_sub.title, url=random_sub.url, description=f':arrow_up:  **Upvotes:** {random_sub.score:,}', color=color_reddit)
                    
        embed.set_image(url=random_sub.url)
                    
        embed.set_author(name=f'u/{random_sub.author.name}', url=f'https://reddit.com/user/{random_sub.author.name}')

        embed.set_footer(text=f'source: r/{random_sub.subreddit.display_name}', icon_url='https://i.imgur.com/sSyG1gH.png')


        await ctx.send(embed=embed)
    

def setup(bot):
    bot.add_cog(Reddit(bot))