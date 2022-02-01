import asyncio, discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
	print("We have loggedd in as {0.user}".format(bot))

@bot.command()
async def 말랑(ctx):
    await ctx.send("말랑쓰")

@bot.command()
async def 개굴프사(ctx):
    await ctx.send("https://images-ext-1.discordapp.net/external/46hUbX-NhJIHwzDtIFhfID8H0SObtJDsHZsIGxh5OOI/%3Fwidth%3D670%26height%3D670/https/media.discordapp.net/attachments/927236972601294848/937914519785721876/21561672c75d67350f1b1924127f7fff.png")


        

bot.run('OTM3NzcxNTY1MjUxMTgyNjQy.Yfgl1A.lqxxK-9BcxDQRTjjtVxK-QbsOi8')
