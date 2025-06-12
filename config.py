# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "28964382"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "c552befc21408d4ef175a66cb44cc33c")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7836392521:AAEEvn5OEybMn2vwm6tTezGh2w_Qy7uuFnw")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("@All_Extractorbot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "6890400066"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6890400066 5744263553").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002594448328"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://user:user1@cluster0.sp0pitj.mongodb.net/")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1002561868621"))

