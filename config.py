from os import getenv
from dotenv import load_dotenv

load_dotenv()


SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))

STREAM_URL=os.environ.get("STREAM_URL", "https://radioindia.net/radio/hungamanow/icecast.audio")
ADMIN = os.environ.get("ADMINS", '')
ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    
