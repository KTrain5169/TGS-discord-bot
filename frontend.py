import discord
import os
from bot_code.backend import handle_ping_command
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

    # Check for the "!ping" command and call the backend function
    if message.content.startswith('!ping'):
        latency = client.latency  # Get bot's latency
        response = handle_ping_command(latency)  # Call backend function with latency
        await message.channel.send(response)

# Run the bot with the token stored in the environment
client.run(os.getenv("DISCORD_TOKEN"))
