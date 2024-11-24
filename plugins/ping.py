from pyrogram import Client, filters
import time


@Client.on_message(filters.private & filters.command(['ping', 'alive']))
async def ping(bot, message):
    start_t = time.time()
    await message.reply_text("Pong!")
    end_t = time.time()
    ping_time = (end_t - start_t) * 1000
    await message.reply_text(f"Ping: {ping_time:.2f} ms")
