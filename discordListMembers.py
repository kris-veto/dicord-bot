import os #se usa para interactuar con el sistema operativo, como leer variables de entorno
import discord   #biblioteca que permite interactuar con la API de Discord.
from dotenv import load_dotenv  # permite cargar variables de entorno desde un archivo .env, que es útil para mantener seguros tokens y otras credenciales.

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")  #Este token es esencial para que tu bot se autentique y se conecte a Discord.
# TOKEN = 'MTIyMDM1NzE0ODAzMTA1Nzk0MA.GILvLX.5abAqmCB-TMJ-skFIK0il76pcMcfYXE22ptnto'
GUILD = os.getenv("DISCORD_GUILD") # Load the guild from the env file //   esta línea lee el nombre del servidor de Discord desde una variable de entorno, permitiendo que el script sepa en qué servidor operar.
# GUILD = 'Pythonw24-bot-A3'

# Create discord client
client = discord.Client(intents=discord.Intents.all())#Crea un objeto client que representa nuestro bot.
#Los intents especifican qué eventos y tipos de datos el bot puede acceder. 


@client.event ##Este decorador y función asincrónica se llaman automáticamente cuando el bot ha terminado de iniciar y está listo para trabajar.
async def on_ready(): #esta funcion define qué debe hacer el bot una vez que esté en línea.
    
    #print(TOKEN)
    #print(GUILD)
    guild = discord.utils.get(client.guilds, name=GUILD) # In case we are connected to multiple guilds, we can select the active guild with our env file
    #print(guild) 
    print(f"{client.user} is online on {guild.name}!")
    members = ""
    for member in guild.members: #list of members in my server
        members += f"\n{member.name},{member.joined_at}"
        members += "\n - " + member.name
    #print("Member joined at:", member.joined_at)   
    
    print("Current members are:" + members)

# Run the bot
client.run(TOKEN)