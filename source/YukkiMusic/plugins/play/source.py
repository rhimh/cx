import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
from config import BANNED_USERS, MUSIC_BOT_NAME

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")


@app.on_message(
    command(["سورس فراوله","سورس","السورس","يا سورس"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://t.me/ghgghghghg/14",
        caption=f"""[ωᥱℓᥴ᥆ꪔᥱ ᥉υ᥆ᖇᥴᥱ ƒᥲ️︎ᖇᥲ️︎ωℓᥲ️︎🎸](https://t.me/SSSSMY)\n\n[✘ 𝘼𝘽𝙊𝙈𝘼𝙕𝙀𝙉 ✘ 🎸](https://t.me/CU_C1)\n\n[✘ 𝗔𝗛𝗠𝗘𝗗  ✘🎸](https://t.me/AM_RKY)\n\n[بوت التواصل 🎸](https://t.me/CUQ3BOT)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✘ 𝘼𝘽𝙊𝙈𝘼𝙕𝙀𝙉 ✘", url=f"https://t.me/CU_C1"), 
                ],[
                    InlineKeyboardButton(
                        "✘ 𝗔𝗛𝗠𝗘𝗗  ✘", url=f"https://t.me/AM_RKY"),
                ],[
                InlineKeyboardButton(
                        "بوت التواصل", url=f"https://t.me/CUQ3BOT"),
                ],[
                InlineKeyboardButton(
                        "قناة السورس⚡", url=f"https://t.me/SSSSMY"),
                ],[
                    InlineKeyboardButton(
                        "أضغط لاضافه ألبوت لمجموعتك 𖣳", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                ],

            ]

        ),

    )
