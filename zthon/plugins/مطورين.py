import zthon
from zedthon import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from zedthon import zedthon


@app.on_message(
    command(["المطورين","عبد الاله"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/8339c0d3a0025c03ee731.jpg",
        caption=f"""• | مطورين سورس عبد الاله""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "عبد الاله ", url=f"https://t.me/h_v_i"),
                    InlineKeyboardButton(
                        "عبد الاله ♡", url=f"https://t.me/h_v_i"),
                ],
                [
                   InlineKeyboardButton(
                        "Leader ", url=f"https://t.me/PP_NL"),
                ],       
            ]
        ),
    )
    
