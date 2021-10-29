from pymongo import MongoClient
from BD import DB_URL, BOT_ID, tbot
from telethon.sync import events


@tbot.on(events.ChatAction(func=lambda e: e.user_added and e.user_id == BOT_ID))

db = MongoClient(DB_URL)["bdbotto"]