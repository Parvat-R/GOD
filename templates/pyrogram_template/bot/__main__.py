from pyrogram import Client
import os


client = Client(
    ":memory:",
    api_id=os.environ.getenv("API_ID"),
    api_hash=os.environ.getenv("API_HASH"),
    bot_token=os.environ.getenv("BOT_TOKEN")
)


if __name__ == "__main__":
    client.run()