
from pyrogram import Client

class Bot:
    def __init__(self):
        self.client = Client(
            "xsfilesxbot",  # Yahaan par name parameter zaroor dena hoga
            api_id="your_api_id",
            api_hash="your_api_hash",
            bot_token="your_bot_token"
        )

    def run(self):
        self.client.run()
     
