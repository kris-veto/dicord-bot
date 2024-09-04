import os
import discord
from dotenv import load_dotenv

# Load discord token from environment
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
# TOKEN = 'MTIyMDM1NzE0ODAzMTA1Nzk0MA.GILvLX.5abAqmCB-TMJ-skFIK0il76pcMcfYXE22ptnto'
# Create discord client
client = discord.Client(intents=discord.Intents.default()) # Intents change what events our bots can respond to, for now we will use the default

@client.event # This is called a "Decorator" it signifies that this method responds to a client event with the same name as the function
async def on_ready():
    guild = client.guilds[0] # Because we are only connected to one Guild, we can get the first guild in the "guilds" list
    print(f"{client.user} is online on {guild.name}!") # Prints a message to the console when a successfuly connection is made

# Run the bot
client.run(TOKEN)