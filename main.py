from bot import Bot
import pyrogram.utils

# MIN_CHANNEL_ID ko customize karein, yadi zarurat ho
pyrogram.utils.MIN_CHANNEL_ID = -1009147483647

# Bot class ko run karein
Bot().run()
