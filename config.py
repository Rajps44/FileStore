#(©)t.me/CodeFlix_Bots




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7318176377:AAEuD9V_QshZXidOESU4jMiCA0rdzbHkjAM")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "29364664"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "c1f087d9a81e97167013615824a7496c")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002132781157"))
# NAMA OWNER
OWNER = os.environ.get("OWNER", "sanjusenxryz")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7451167149"))
#Port
PORT = os.environ.get("PORT", "8030")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://sanjusen321:VQOwwonR4pBeNyal@cluster0.1osdd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002085077648"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://i.postimg.cc/tgj9XNhg/IMG-20240827-170934-646.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "")


START_MSG = os.environ.get("START_MESSAGE", "<b>Hello!! {first}\n\n I can store private files in Specified Channel and other users can access it from special link.</b>")

try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "6174868004 6803963354 7451167149").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @netfilix_movie</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Hii sir  ! YOU ARE NOT MY OWNER!!"

ADMINS.append(OWNER_ID)
ADMINS.append(7451167149)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
