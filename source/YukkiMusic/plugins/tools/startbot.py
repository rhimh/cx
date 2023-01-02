import sys
import asyncio
import requests
import re
import string
from pyrogram.types import Message
from aiohttp import ClientSession
from pyrogram import filters, Client
from strings import get_command
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from config.config import START_IMG_URL
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


#استارت
@app.on_message(
    filters.command(["الاوامر","اوامر","/help"],""))
async def italy(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_IMG_URL}",
        caption=f"""✅ **مرحبا بك عزيزي** {message.from_user.mention}
     
✅ **اليك قائمة اوامر سورس فراولة ♬**
•▬▭࣪▬•| ♬ ᥉υ᥆ᖇᥴᥱ ƒᥲ️︎ᖇᥲ️︎ωℓᥲ️︎ ♬ |•▬▭࣪▬•
**1 ← اوامـر الـمـجـمـوعـات .**
**2 ← اوامـر الـبـوت .**
**3 ← مميزات السورس .**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "◁ الـمـجـمـوعـات ▷", callback_data=f"italygro"),
                ],[
                InlineKeyboardButton(
                        "◁ الـبـوت ▷", callback_data=f"italybot"),
                ],[
                    InlineKeyboardButton(
                        "♬ ᥉υ᥆ᖇᥴᥱ ƒᥲ️︎ᖇᥲ️︎ωℓᥲ️︎ ♬", callback_data=f"italydev"),
                ],[
                    InlineKeyboardButton(
                        "اغــلاق ♬", callback_data=f"close"),
               ],
            ]
        ),
    )
#كول باك اوامر المجموعه
@app.on_callback_query(filters.regex("italygro"))
async def italy(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""✅ **اليك قائمة اوامر المجموعات ♬**
•▬▭࣪▬•| ♬ ᥉υ᥆ᖇᥴᥱ ƒᥲ️︎ᖇᥲ️︎ωℓᥲ️︎ ♬ |•▬▭࣪▬•
**- لتشغيل اغنيه اكتب : تشغيل او شغل .**
**- لتشغيل فيديو اكتب : فيديو .**
**- لأنهاء الاغنيه اكتب : ايقاف او انهاء .**
**- لتخطي الاغنيه اكتب : تخطي .**
**-اذا حدث خطأ او اعادة التشغيل اكتب :** /restart .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁ الـبـوت ▷", callback_data=f"italybot"),
                ],[
                    InlineKeyboardButton(
                        "♬ ᥉υ᥆ᖇᥴᥱ ƒᥲ️︎ᖇᥲ️︎ωℓᥲ️︎ ♬", callback_data=f"italydev"),
                ],[
                    InlineKeyboardButton(
                        "اغــلاق ♬", callback_data=f"close"),
               ],
            ]
        ),
    )

#كول باك اوامر البوت
@app.on_callback_query(filters.regex("italybot"))
async def italy(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""✅ **اليك قائمة اوامر الـبـوت ♬**
•▬▭࣪▬•| ♬ ᥉υ᥆ᖇᥴᥱ ƒᥲ️︎ᖇᥲ️︎ωℓᥲ️︎ ♬ |•▬▭࣪▬•
**- لعمل اذاعه في البوت قم برد علي الاذاعه واكتب : اذاعه .**
 **- لعرض احصائيات البوت اكتب : الاحصائيات .**
**- لعرض سرعه البوت اكتب : بينج .**
**- للتحكم في لغه البوت اكتب : اللغه .**
**- للتحكم في وضع التشغيل اكتب : الاعدادات .**
**- اوامر الحظر والرفع في كيبورد المطور .**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "◁ الـمـجـمـوعـات ▷", callback_data=f"italygro"),
                ],[
                    InlineKeyboardButton(
                        "♬ ᥉υ᥆ᖇᥴᥱ ƒᥲ️︎ᖇᥲ️︎ωℓᥲ️︎ ♬", callback_data=f"italydev"),
                ],[
                    InlineKeyboardButton(
                        "اغــلاق ♬", callback_data=f"close"),
               ],
            ]
        ),
    )
#كول باك المطورين
@app.on_callback_query(filters.regex("italydev"))
async def ayamr(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""[ٓ♡ | 𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 𝑆𝑂𝐔𝑅𝐶𝐸 .](https://t.me/SSSSMY)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "♬ ᥉υ᥆ᖇᥴᥱ ƒᥲ️︎ᖇᥲ️︎ωℓᥲ️︎ ♬", url=f"https://t.me/SSSSMY"),
                ],[ 
                InlineKeyboardButton(
                        "✘ ||𝘼𝘽𝙊𝙈𝘼𝙕𝙀𝙉|| ☬『 مــ ـٰٖمـوِٰلٰ 』", url=f"https://t.me/CU_C1")
                ],[
                    InlineKeyboardButton(
                        "رجــوع ♬", callback_data=f"italyback"),
               ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("italyback"))
async def italy(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""✅ **اليك قائمة اوامر سورس فراولة ♬**
•▬▭࣪▬•| ♬ ᥉υ᥆ᖇᥴᥱ ƒᥲ️︎ᖇᥲ️︎ωℓᥲ️︎ ♬ |•▬▭࣪▬•
**1 ← اوامـر الـمـجـمـوعـات .**
**2 ← اوامـر الـبـوت .**
**3 ← مميزات السورس .**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "◁ الـمـجـمـوعـات ▷", callback_data=f"italygro"),
                ],[
                InlineKeyboardButton(
                        "◁ الـبـوت ▷", callback_data=f"italybot"),
                ],[
                    InlineKeyboardButton(
                        "♬ ᥉υ᥆ᖇᥴᥱ ƒᥲ️︎ᖇᥲ️︎ωℓᥲ️︎ ♬", callback_data=f"italydev"),
                ],[
                    InlineKeyboardButton(
                        "اغــلاق ♬", callback_data=f"close"),
               ],
            ]
        ),
    )
