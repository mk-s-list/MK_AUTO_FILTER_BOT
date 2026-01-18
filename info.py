import os

# ─── Telegram ───
API_ID = int(os.getenv("API_ID", "123456"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# ─── Database ───
MONGO_URI = os.getenv("MONGO_URI", "")
DB_NAME = os.getenv("DB_NAME", "file_store")

# ─── Owner / Admin ───
OWNER_ID = int(os.getenv("OWNER_ID", "0"))
ADMINS = [int(x) for x in os.getenv("ADMINS", "").split() if x]

# ─── Channels / Logs ───
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "0"))
FILE_CHANNEL = int(os.getenv("FILE_CHANNEL", "0"))

# ─── Force Subscribe ───
F_SUB_CHANNEL = int(os.getenv("F_SUB_CHANNEL", "0"))

# ─── Links / Limits ───
START_PIC = os.getenv("START_PIC", "")
MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", "2147483648"))  # 2GB

# ─── IMDB ───
IMDB_API = os.getenv("IMDB_API", "")
IMDB_TEMPLATE = os.getenv("IMDB_TEMPLATE", "{title} ({year})")

# ─── Shortlink ───
SHORTLINK_API = os.getenv("SHORTLINK_API", "")
SHORTLINK_DOMAIN = os.getenv("SHORTLINK_DOMAIN", "")

# ─── Premium ───
PREMIUM_DAYS = int(os.getenv("PREMIUM_DAYS", "30"))

# ─── Misc ───
BOT_USERNAME = os.getenv("BOT_USERNAME", "")