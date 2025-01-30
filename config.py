import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "28625021"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f1334d4192baa39e5fb10147559a354d")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6073523936"))

mongodb+srv://nraajfcs:WD5jN3tdgJCNTd5n@cluster0.2x487.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
