import discord
import os
from flask import Flask
from threading import Thread

# Discord bot setup
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Web server setup to keep the bot alive
app = Flask('')

@app.route('/')
def home():
    return "Hello, I am alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Discord bot events
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello! 👋')

# Run the keep_alive server
keep_alive()

# Run the bot
client.run(os.getenv("DISCORD_TOKEN"))
