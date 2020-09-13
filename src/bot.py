import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

class SocialBot(commands.Bot):
    def __init__(self):
        self.token = TOKEN
        super().__init__(commands.when_mentioned_or('&'))
        #modules for each social media service
        self.load_extension('cogs.whatsapp')


bot = SocialBot()

@bot.event
async def on_ready():
    print("Ready to socialize")

bot.run(bot.token)
