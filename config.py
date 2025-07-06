# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = os.getenv("API_ID", "20708013")
API_HASH = os.getenv("API_HASH", "f0dbe59c7e43cc49fe9e83206ef9f828")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7895412742:AAFAb3dsuce_JvKe85332oF6eyOwK9D3PaM")
MONGO_DB = os.getenv("MONGO_DB", "mongodb+srv://saved:saved@cluster0.r0js63z.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "1188631841").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "telegram_downloader")
STRING = os.getenv("STRING", None) # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", "-1002768582112")) # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", -1002376025556")) # optional with -100
MASTER_KEY = os.getenv("MASTER_KEY", "34924327c41ff8e7ad6334782f0198c6") # for session encryption
IV_KEY = os.getenv("IV_KEY", "d9c4f17f682a") # for decryption
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "2"))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT", "500"))
JOIN_LINK = os.getenv("JOIN_LINK", "https://t.me/MUNNAKIHWELI") # this link for start command message
ADMIN_CONTACT = os.getenv("ADMIN_CONTACT", "https://t.me/itsmunnabhaiya")
