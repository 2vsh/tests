import discord
from discord.ext import commands
import random

# Set up the bot with a command prefix
bot = commands.Bot(command_prefix="!")

@bot.command()
async def flip(ctx):
    # Choose heads or tails randomly
    result = random.choice(["heads", "tails"])

    # Send the corresponding emoji to the user
    if result == "heads":
        await ctx.send("<:coin_heads:734271973944725505>")
    else:
        await ctx.send("<:coin_tails:734271973583996929>")

# Run the bot
bot.run("YOUR_BOT_TOKEN_HERE")
