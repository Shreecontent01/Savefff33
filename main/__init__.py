#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default=7868296, cast=int)
API_HASH = config("API_HASH", default="bfa7fecb33443243ff8c8b0f27f9cd68")
BOT_TOKEN = config("BOT_TOKEN", default="5394356797:AAGoTNSZZqmDwzT0Bqn1APDZ5_0ueUb4DMo")
SESSION = config("SESSION", default="BABGjQlHSLZ11dA2F-YML5VmdMngcJ9R9Gv8dGkS0Xy5guZEk5yFehxulSGygvNbCgj0lK8KIo61t9Hhg4FshbzTr7pkvRtcm-kuUzxnTz8CCJs7HoZrVRvhCxZ_PYzVj2JoSP9XONRFHMdlDtOKh9DE6fatul58rAhR888rfwPHaSNNCgvHVuA34jJXFMaLQT_T2JHFSW_eAVSqwky4-yet-DPprFQ8-X8bY7BvY6jWtrJNgMoVjy7SlnT36qLI9k2m-PEzT59Tf7ZzRvP5UMi4fghIcPhRWQVdVwBCvPFoJI8z_QqNkalUDWHIzDYDaH8-swF5tBR_QyTdW_Sw7DFOAAAAASq_dygA")
FORCESUB = config("FORCESUB", default=-1001870063718)
AUTH = config("AUTH", default=5012158248, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
