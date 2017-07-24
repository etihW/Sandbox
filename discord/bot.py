import discord
from discord.ext.commands import Bot

my_bot = Bot(command_prefix="!")


@my_bot.event
async def on_read():
    print("Client logged in")
@my_bot.command()
async def hello(*args):
    return await my_bot.say("Hello, world!")

@my_bot.command()
async def test(*args):
    return await my_bot.say("I copy")

@my_bot.command()
async def remember(*args):
    for x in args:
        rememberBox += x
    return await my_bot.say("Okay, I'll remember " + rememberBox)

@my_bot.command()
async def remind(*args):
    return await my_bot.say("Oh yeah! You wanted me to remind you about " + rememberBox)






fn = open("key.txt","r")

my_bot.run(fn.read())
