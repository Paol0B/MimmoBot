import discord

# Crea un'istanza del client Discord
client = discord.Client()

# Quando il bot viene avviato, esegue questa funzione
@client.event
async def on_ready():
    print("Il bot è pronto!")

# Quando il bot riceve un messaggio, esegue questa funzione
@client.event
async def on_message(message):
    # Se il messaggio proviene da un utente
    if message.author != client.user:
        # Se il messaggio contiene il comando "ping", risponde con "pong"
        if message.content.startswith("ping"):
            await message.channel.send("pong")

# Avvia il bot
client.run("TOKEN")
