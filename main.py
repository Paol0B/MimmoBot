import asyncio

import discord

import function

# Token del bot
TOKEN = ""

# Crea un'istanza del bot
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("The bot is ready.")

@client.event
async def on_member_join(member):
    channel = member.voice.channel
    await channel.connect()

@client.event
async def on_voice_state_update(member, before, after):
    if after.channel is not None and before.channel is None:
        channel = member.voice.channel
        await channel.connect()

@client.event
async def on_message(message):
    # Controlla se il messaggio contiene il comando `/3060`
    if message.content.startswith("/3060"):
        # Ottieni l'utente che ha scritto il messaggio
        member = message.author

        # Ottieni il canale vocale in cui si trova l'utente
        channel = member.voice.channel

        # Entra in chiamata
        await channel.connect()
        await listen_and_disconnect(client)
    elif message.content.startswith("/pepsi"):
        await message.guild.voice_client.disconnect()

async def listen_and_disconnect(client):
    # Ascolta in loop
    print("Listening for 3060...")
    while True:
        # Ascolta per 5 secondi
        await asyncio.sleep(5)

        # Ottieni l'audio del client
        audio = client.voice_client.recv()

        # Converti l'audio in testo
        text = client.voice_client.recognize_speech(audio)

        # Controlla se il testo contiene la parola "3060"
        if text.lower().find("3060") != -1:
            # Disconnetti l'utente che ha pronunciato la parola
            await client.voice_client.disconnect()


client.run(TOKEN)