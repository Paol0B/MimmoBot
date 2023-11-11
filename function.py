import asyncio

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