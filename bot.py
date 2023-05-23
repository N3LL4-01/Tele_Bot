from pyrogram import Client
from faker import Faker
import time
import random
import locale
 
fake = Faker('ru_RU')  # Faker mit ru_RU-Locale initialisieren
 
BOT_NAME = "@contractMObot" # füge hier den Bot ein 
app = Client("spam", api_id=, api_hash="")
print("Wie viele Durchgänge soll ich machen?")
count = int(input(">>> "))
 
def run():
    with app:
        # Start the conversation
        app.send_message(BOT_NAME, "/start")
        time.sleep(2)  # Let the bot respond
 
        # Agree to the terms
        app.send_message(BOT_NAME, "Согласен") # falls eine GUI abfrage erfordert wird
        time.sleep(2)
 
        # Send the fake name
        app.send_message(BOT_NAME, fake.name())
        time.sleep(2)
 
        # Send a random age
        app.send_message(BOT_NAME, str(random.randint(18, 70)))
        time.sleep(2)
 
        # Send the fake address
        app.send_message(BOT_NAME, fake.address())
        time.sleep(2)
 
        # Send the fake phone number
        app.send_message(BOT_NAME, f"+7 (946) 464-64-64")
        time.sleep(2)
 
        # Send the fake email
        app.send_message(BOT_NAME, fake.email())
        time.sleep(2)
 
        # Confirm the correctness
        app.send_message(BOT_NAME, 'Да, все верно')
 
for i in range(count):
    run()
    if (i + 1) % 100 == 0:
        print(f"Durchgang {i+1} abgeschlossen. Pause für 5 Minuten...")
        time.sleep(300)  # Pause für 5 Minuten (300 Sekunden)
