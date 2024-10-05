import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config

bot = Client(
    "bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

ON_SUCCESS_POST = """
✅ Pesan Kamu telah berhasil dikirim ke channel. Lihat di sini:
"""

@bot.on_message(
	(filters.text | filters.photo | filters.video | filters.audio | filters.voice) &
	filters.private)
async def on_post_menfess(_, m: Message):
	user = m.from_user
	ch_usn = os.getenv("CHANNEL_USERNAME")

	copied = await m.copy(ch_usn)
	await m.reply(
		text=ON_SUCCESS_POST,
		reply_markup=InlineKeyboardMarkup(
			[[InlineKeyboardButton(
				"Lihat pesan 💬",
				url=f"t.me/{ch_usn}/{copied.id}"
			)]]
		),
		disable_web_page_preview=True,
		disable_notification=True
	)
