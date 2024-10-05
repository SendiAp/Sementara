
@bot.on_message(
	(filters.text | filters.photo | filters.video | filters.audio | filters.voice) &
	filters.private)
async def on_post_menfess(_, m: Message):
	user = m.from_user
	ch_usn = os.getenv("CHANNEL_USERNAME")

	copied = await m.copy(ch_usn)
	await m.reply(
		text=ON_SUCCESS_POST.format(user_id=user.id),
		reply_markup=InlineKeyboardMarkup(
			[[InlineKeyboardButton(
				"Lihat pesan 💬",
				url=f"t.me/{ch_usn}/{copied.id}"
			)]]
		),
		disable_web_page_preview=True,
		disable_notification=True
	)
