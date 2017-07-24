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
    f = open("remember.txt", "w+")
    
    for x in args:
        if x == args[-1]:
            f.write(x)
        else:
            f.write(x + " ")
    f.close()
    f = open("remember.txt", "r")
    return await my_bot.say("Okay, I'll remember " + f.read())

@my_bot.command()
async def remind(*args):
    f = open("remember.txt", "r")
    return await my_bot.say("Oh yeah! You wanted me to remind you about " + f.read())






fn = open("key.txt","r")

my_bot.run(fn.read())
