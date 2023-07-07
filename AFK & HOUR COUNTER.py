import discord, random, os, time
from discord.ext import commands
 
input("Welcome User! Press Enter To Continue...")
os.system('cls')
token = input("Enter Your Discord Token Here: ")
client = commands.Bot(command_prefix=commands.when_mentioned_or("$"))
os.system('cls')
os.system(f'title [AFK CHECKER AND HOUR COUNTER BY YERSUH]')
os.system(f'mode 60,20')
 


 
@client.event
async def on_ready():
  print(f""" \u001b[31m
█░█ █▀█ █░█ █▀█   ▄▀█ █▀▀ █▄▀
█▀█ █▄█ █▄█ █▀▄   █▀█ █▀░ █░█
logged in {client.user}
THIS IS A HOUR COUNTER, AND AN AFK COUNTER

TYPE "start" TO START THE HOUR COUNTER ( DOES HOURS FOR YOU )

TYPE "afk" TO START THE AFK CHECKER ( STARTS AT 2 )
------------------------------
""")
 
@client.event
async def on_message(message):
    channel = message.channel
    if message.content.startswith('start'):
        for i in range(1, 100001):
            if i % 1 == 0:
                time.sleep(3600)
            await channel.send(i)

@client.event
async def on_message(message):
    channel = message.channel
    if message.content.startswith('afk'):
      for i in range(2, 100001):
        await message.channel.send(i)
        if i > 29:
          time.sleep(1.7)

 
client.run(token, bot=False)
