from bot import Bot

if __name__ == "__main__":
    try:
        # Initialize and run the bot
        Bot().run()
    except Exception as e:
        print(f"Error occurred: {e}")
