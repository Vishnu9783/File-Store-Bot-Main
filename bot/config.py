from datetime import datetime
import os
from dotenv import load_dotenv
from pyrogram.types import InlineKeyboardButton


if os.path.exists("config.env"):
    load_dotenv("config.env")
else:
    load_dotenv()


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


class Config(object):
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    OWNER_ID = int(os.environ.get("OWNER_ID"))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "0"))
    REDIRECT_WEBSITE = os.environ.get("REDIRECT_WEBSITE", None)
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "advancefiletestbot")
    WEB_SERVER = is_enabled(os.environ.get("WEB_SERVER", "False"), False)
    CHANNELS = int(os.environ.get("CHANNELS", "0"))


class Script(object):
    START_MESSAGE = """Hi, {mention}, Welcome to our Movie and Webseries Provider Bot.
Exclusively work for VIP Studios.

Exclusive Content, VIP Experience."""

    HELP_MESSAGE = os.environ.get(
        "HELP_MESSAGE",
        "This is a file, videos, images, audio saver bot with some advanced features",
    )

    NEW_USER_MESSAGE = """#NewUser

🧾 Name : {mention}
👤 User Id : `{user_id}`"""

    NOT_ALLOWED_TEXT = "You are not allowed to send text messages here."
    ARROGANT_REPLY = "You are not my father, don't try to play with me"
    ABOUT_MESSAGE = f"""○ 𝖢𝗋𝖾𝖺𝗍𝗈𝗋 : <a href='tg://user?id={Config.OWNER_ID}'>𝖳𝗁𝗂𝗌 𝖯𝖾𝗋𝗌𝗈𝗇</a>\n○ 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 : <code>𝖯𝗒𝗍𝗁𝗈𝗇 𝟥</code>\n○ 𝖲𝗈𝗎𝗋𝖼𝖾 𝖢𝗈𝖽𝖾 : <a href='tg://user?id={Config.OWNER_ID}'>𝖯𝖺𝗂𝖽</a>\n○ 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 : <a href='https://t.me/Vip_studios'>𝖵𝖨𝖯 𝖲𝗍𝗎𝖽𝗂𝗈𝗌</a>\n○ 𝖲𝗎𝗉𝗉𝗈𝗋𝗍 𝖦𝗋𝗈𝗎𝗉 : <a href='https://t.me/+UoOAfvRc8R0zNjg1'>𝖣𝗂𝗌𝖼𝗎𝗌𝗌𝗂𝗈𝗇 𝖢𝗁𝖺𝗍</a>"""


class Buttons(object):
    START_BUTTONS = [
        # "force subscribe" button
        [
            InlineKeyboardButton("Force Subscribe", callback_data="force_sub_config"),
        ],
        [
            InlineKeyboardButton("Auto Delete", callback_data="auto_delete_config"),
        ],
        [
            InlineKeyboardButton("💡 Help", callback_data="help"),
        ],
    ]
    BACK_BUTTON = [[InlineKeyboardButton("☜ Back", callback_data="start")]]
    USER_START_BUTTONS = [
        [
            InlineKeyboardButton("About Me", callback_data="about"),
            InlineKeyboardButton("Close", callback_data="close"),
        ],
    ]


class CONST(object):
    START_TIME = datetime.now()
