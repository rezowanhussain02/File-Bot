import os
from dotenv import load_dotenv
from pyrogram import Client

# Load environment variables from the .env file
load_dotenv()

# Read credentials from environment variables
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

class Bot(Client):
    def __init__(self):
        # Initialize the Pyrogram Client with the credentials
        super().__init__(
            "FileBot",
            api_id=api_id,
            api_hash=api_hash,
            bot_token=bot_token,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        print(f"Bot started as @{me.username}")

    async def stop(self, *args):
        await super().stop()
        print("Bot stopped")

    async def run(self):
        await self.start()
        print("Bot is running...")
        await self.idle()
        await self.stop()
