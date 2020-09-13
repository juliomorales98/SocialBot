import discord
import pywhatkit as kit
import threading
from discord.ext import commands

def setup(bot):
    bot.add_cog(Whatsapp(bot))

class Whatsapp(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def hw(self,ctx):
        await ctx.send("Hello from whatsapp cog")

    def thread_wp_send(self,message,numner,hour,minutes):
        kit.sendwhatmsg(number,message,hour,minutes)

    @commands.command()
    async def wp_send(self,ctx, message,number,hour:int,minutes:int):
        t = threading.Thread(target=self.thread_wp_send, args=(message,hour,minutes))
        t.start()

    
