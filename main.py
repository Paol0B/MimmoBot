import discord
import pyaudio
import speech_recognition as sr

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Il bot è pronto!")

@client.event
async def on_message(message):
    if message.author != client.user:
        if message.content.startswith("ping"):
            await message.channel.send("pong")

# Avvia il bot
async def on_ready():
    print("Il bot è pronto!")

# Crea un'istanza di pyaudio
p = pyaudio.PyAudio()

# Crea un flusso di input audio
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

# Funzione che ascolta e riconosce la parola "3060"
async def ascolta(utente):
    while True:
        # Legge l'audio
        audio_data = stream.read(1024)

        # Tenta di riconoscere la parola "3060"
        try:
            # Rileva la parola "3060"
            parola_riconosciuta = speech_recognition.recognize_google(audio_data)

            # Se la parola è "3060", disconnette l'utente che l'ha pronunciata
            if parola_riconosciuta == "3060":
                # Disconnette l'utente
                await utente.edit(voice_channel=None)

        # Se c'è stato un errore nel riconoscimento vocale
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass

# Avvia la funzione che ascolta
@client.event
async def on_message(message):
    if message.author != client.user:
        if message.content.startswith("ping"):
            await message.channel.send("pong")

# Avvia la funzione che ascolta
client.loop.create_task(ascolta(message.author))

client.run("MTE3MjYzMTE4Nzk2NjE0MDUyNw.GmxcoS.NN-WCbGlqloXc5we17kfTs-dLkqrMvbIEGMYQs")
