import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
     command(["ابو مازن"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/308381571a0da445373d5.jpg",
caption=f"""**▷✘ ||𝘼𝘽𝙊𝙈𝘼𝙕𝙀𝙉|| ☬『 مــ ـٰٖمـوِٰلٰ 』 ♯**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                    "CHANNEL", url=f"https://t.me/ssssmy"
                ),
                ],
                [
                    InlineKeyboardButton(
                        "✘ ||𝘼𝘽𝙊𝙈𝘼𝙕𝙀𝙉|| ☬『 مــ ـٰٖمـوِٰلٰ 』", url=f"https://t.me/CU_C1"),
                ],
            ]
        ),
    )
