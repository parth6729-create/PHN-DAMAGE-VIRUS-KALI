import discord
from discord.ext import commands

# Enable intents
intents = discord.Intents.default()
intents.message_content = True  # Needed to read messages
intents.members = True          # Needed for member info

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run("MTQ3MTgyNzAzOTUyNjA2NDE1OQ.GiKiVq.hzT4iKQcl15q1Rd2dcAY3vZquV_JT_47I6KX-g")
