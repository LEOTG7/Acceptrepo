from os import path, getenv
import os, time 
#from pyrogram.types import BotCommand

class Config:
    API_ID = int(getenv("API_ID", "23100424"))
    API_HASH = getenv("API_HASH", "377181507ef31b3ceef9fd6733756feb")
    BOT_TOKEN = getenv("BOT_TOKEN", "7004962339:AAFauWpInLvn1JUjEbTjSnacSQXlnCfRvd8")
    UPDATE_CHANNEL = getenv("UPDATE_CHANNEL", "XoMovies")
    UPDATECHANNEL_ID = int(getenv("UPDATECHANNEL_ID", "-1001886672413"))
    ADMIN = list(map(int, getenv("ADMIN", "1242556540").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://XoBruce:BsjBIPIQIRVBKNON@xobruce.ubqor0m.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-2132087730"))
    
    #web response 
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    BOT_UPTIME  = time.time()
    PORT = os.environ.get("PORT", "8080")
    
    DP_PIC = os.environ.get("DP_PIC", "https://graph.org/file/67a5c787deb0d67fd3f69.jpg")
    BOT_USERNAME = os.environ.get("BOT_USERNAME","TeamXo_Auto_Approve_Bot")
 # Subsprice Gif & Auto Request Accept
    SURPRICE = os.environ.get("SURPRICE", "https://graph.org/file/67a5c787deb0d67fd3f69.jpg").split()

    LOGO = """DP_BOTZ"""

dp1 = Config()