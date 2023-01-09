from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import hi_command
from bot_commands import time_command
from bot_commands import help_command
from bot_commands import sum_command


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5916104085:AAGZ-5CJWTi-x2IMrE6XH2dlfuO04Ts_Npg").build()

app.add_handler(CommandHandler("Hi", hi_command))
app.add_handler(CommandHandler("Time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

app.run_polling()