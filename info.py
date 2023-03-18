import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = '8827228'
API_HASH = "db66c22b8e630b12cd0b3823c610b3c2"
BOT_TOKEN = "5687433271:AAH7ke2ctZQIRhXhlN3APoEh0z9yTe7Jvgw"

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/FILO-PICS-01-26 https://telegra.ph/FILO-02-01-26 https://telegra.ph/FILO-03-01-26 https://telegra.ph/FILO-03-01-26-2 https://telegra.ph/FILO-05-01-26')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1979355984').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001733173292').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = "-1001868033481"
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://FILO:FILO@cluster0.rvwnqye.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "LazyDeveloper")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1001862407850))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'LazyDeveloper')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "False")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "⚡<b>File uploaded by [Movies Adaa™](https://t.me/real_MoviesAdda2)</b>⚡\n\n🎦 <b>File Name: </b> ➥  <i>{file_caption}</i>\n⚙️ <b>Size: </b><i>{file_size}</i>\n\n                ❤️<b>WE LOVE YOU</b>❤️\n🔥  ↭ <b>Join Now [MoviesAdda™](https://t.me/real_MoviesAdda2)</b> ↭  🔥")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Your Query: {query}</b> \n‌‌‌‌IMDb Data by: @LazyDeveloper \n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10 \n\n♥️ we are nothing without you ♥️ \n\n💛 Please Share Us 💛\n\n⚠️Click on the button 👇 below to get your query privately")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), False)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "True")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)

#LazyRenamer Configs
FLOOD = int(environ.get("FLOOD", "10"))
LAZY_MODE = bool(environ.get("LAZY_MODE"))
#Add user id of the user in this field those who you want to be Authentic user for file renaming features
lazy_renamers = [int(lazrenamers) if id_pattern.search(lazrenamers) else lazrenamers for lazrenamers in environ.get('LAZY_RENAMERS', '').split()]
LAZY_RENAMERS = (lazy_renamers + ADMINS) if lazy_renamers else []
REQ_CHANNEL = int(environ.get('REQ_CHANNEL'))

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
