from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hello {message.from_user.first_name}!
I am 𝗖𝗵𝗼𝗰𝗼𝗹𝗮𝘁𝘆𝗤𝘂𝗲𝗲𝗻𝗕𝗼𝘁 VC Music Player, an open-source bot that lets you play music in your Telegram groups.
Maintained by @sangramghangale ❤
For source code Join our support group @TeLeTiPsOfficialOnTopicChat.
Use the buttons below to know more about me.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Command", url="https://telegra.ph/𝙰ₚₐᵣᵢₕᵢₜₕₐ𝙽𖧷-04-13",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👥 Group", url="https://t.me/TeLeTiPsOfficialOnTopicChat"
                    ),
                    InlineKeyboardButton(
                        "💾 Source code", url="https://github.com/sangramghangale/VCPlayerBot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Join Channel", url="https://t.me/TeLeTiPsOfficialchannel"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
