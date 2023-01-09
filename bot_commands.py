from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import spy_command

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    spy_command(update,context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    spy_command(update,context)
    await update.message.reply_text(f'Time: {datetime.datetime.now().time()}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    spy_command(update,context)
    await update.message.reply_text(f'/Hi\n/Time\n/help\n/sum!')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    spy_command(update,context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')