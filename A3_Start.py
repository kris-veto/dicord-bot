import os
import discord
from dotenv import load_dotenv
from datetime import datetime
import csv



load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
fname = "memberLogon.csv"

# intents = discord.Intents.default()
# intents.members = True

client = discord.Client(intents=discord.Intents.all())

@client.event 
async def on_ready():
    global fname
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(f"{client.user} is online on {guild.name}!")
    
    general = discord.utils.get(guild.channels, name="general")
    await general.send(f"{client.user} is online ouun {guild.name}!")
    
    if not os.path.exists(fname):
        
        f = open("memberLogon.csv", 'a', newline='')
        writer = csv.writer(f)
        writer.writerow(["Username", "Join Date"])
        for member in guild.members: #list of members in my server
            writer.writerow([member.name, member.joined_at])
            print("Current memberss are:" + str(member))
        f.close()
    
    
@client.event
async def on_member_join(member):
    global fname 
    guild = discord.utils.get(client.guilds, name=GUILD)
    general = discord.utils.get(guild.channels, name="general")
    await general.send(f"Hello {member.name}, welcome to {guild.name}!")
    print(f"{client.user} is online on {guild.name}!")
    
    
    f = open("memberLogon.csv", 'a', newline='')
    writer = csv.writer(f)
    print(f"{client.user} is online on {guild.name}!")
                       
    writer.writerow([member.name, member.joined_at])
    print("A new member has joined: " + str(member))
        
    f.close()
           
    
@client.event
async def on_member_remove(member):
    
    
    print(f"The member {member.name} has left the serverrrrrr.")


client.run(TOKEN)