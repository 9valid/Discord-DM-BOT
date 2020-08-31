import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "$")

class BotData:
    def __init__(self):
        self.welcome_channel = None
        self.goodbye_channel = None

        self.reaction_role = None
        self.reaction_message = None

botdata = BotData()
@bot.event
async def on_ready():
    print("DM BOT IS READY")
    print("NOT OFFICIALLY MADE BY 9VALID")
    print("INSTRUCTIONS IN THE README.MD FILE")


@bot.command()
async def dm_all(ctx, *, args=None):
    if args != None:
        members = ctx.guild.members
        for member in members:
            try:
                await member.send(args)
                print("'" + args + "' sent to: " + member.name)

            except:
                print("Couldn't send '" + args + "' to: " + member.name)

    else:
        await ctx.channel.send("A message.")
        
        ctx.send.message()

bot.run ("TOKEN HERE")