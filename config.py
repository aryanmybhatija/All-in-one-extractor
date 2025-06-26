# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", ""))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("@Image_Uploader1_bot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "8053386100"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8053386100").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002527188402"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://user:user1@cluster0.sp0pitj.mongodb.net/")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1002520864904"))

