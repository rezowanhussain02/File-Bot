from pyrogram import Client

class Bot(Client):
    def __init__(self):
        # Initialize the bot with necessary parameters
        super().__init__(
            "FileBot",
            api_id=int("13567777"),  # Replace with your actual API ID
            api_hash="78df7d20e1a8d17329d38d3095af744f",  # Replace with your actual API hash
            bot_token="7580468323:AAHq1ZRBwsA9yFDz6Xchmw5QXMXom0gDE54",  # Replace with your bot token
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        print(f"Bot started as {me.username}")

    async def stop(self, *args):
        await super().stop()
        print("Bot stopped")

    async def run(self):
        await self.start()
        print("Bot is running...")
        await self.idle()
        await self.stop()
