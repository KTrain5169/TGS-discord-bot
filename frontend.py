import discord
import os
from bot_code.backend import handle_ping_command, get_mod_info
from bot_code.keep_alive import keep_alive

intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Start the web server to keep the bot alive
keep_alive()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # !ping
    if message.content.startswith('!ping'):
        latency = client.latency  # Get bot's latency
        response = handle_ping_command(latency)  # Call backend function with latency
        await message.channel.send(response)

    # !mod
    if message.content.startswith('!mod'):
        _, modname = message.content.split(maxsplit=1)  # Get mod name from command
        response = get_mod_info(modname)  # Call backend function to fetch mod info
        await message.channel.send(response)

# Run the bot with the token stored in the environment
client.run(os.getenv("DISCORD_TOKEN"))
