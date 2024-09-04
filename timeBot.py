import os
import discord
from dotenv import load_dotenv
from datetime import datetime
import aiohttp
import json

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
fname = "memberLogon.csv"

intents = discord.Intents.default()
intents.members = True
intents.message_content = True # Note the new intent, we will need to turn this on in the discord dev portal just like the members intent

client = discord.Client(intents=intents)

@client.event
async def on_message(message):

    # If this bot sent the message, exit to avoid and infinite loop
    if message.author == client.user:
        return

    # If we get the !w -list command, list all available timezones
    if message.content == '!t -list':
        async with aiohttp.ClientSession() as session:
            async with session.get("https://www.timeapi.io/api/TimeZone/AvailableTimeZones") as res:
                responseBody = await res.text()
        timelist = responseBody[1:-1].split(",")

        # this list is really long, shortening it for the example
        timelist = timelist[0:100]

        # Buffered into groups of 20, discord has a message size limit
        await message.channel.send("List of possible time zones:")
        msgBuffer = []
        for timezone in timelist:
            if len(msgBuffer) == 20:
                await message.channel.send("\n -".join(msgBuffer))
                msgBuffer = []
            msgBuffer.append(timezone)
        if len(msgBuffer) > 0:
            await message.channel.send("\n -".join(msgBuffer))

    # If the command is a request for a time zone (note that this does not have error handling!)
    elif message.content[0:4] == "!t -":
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://www.timeapi.io/api/Time/current/zone?timeZone={message.content[4:]}") as res:
                timeObj = json.loads(await res.text()) # convert json into a dictionary
                await message.channel.send(f"DateTime in {message.content[4:]} is {timeObj['dateTime']}")
        
client.run(TOKEN)