# safe_repo
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "25101316"))
API_HASH = getenv("API_HASH", "7a55428e826bc8557889f78a2e1af211")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7990447298").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://Cluster0:Cluster0@cluster0.yhyvn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
