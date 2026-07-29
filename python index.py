import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
from openai import OpenAI

TELEGRAM_TOKEN = os.environ["8829904176:AAEblH5UWNBJQ7ry6tCnaG2tsruzqu7eC7E"]
OPENAI_API_KEY = os.environ["iCacaJbru8haNVeMqDgglpLnMbCJP-IdSr5N_rfItLHq20CyAUFyf6XB-_-LnAwbIlg5A5_WOfT3BlbkFJPHacke-wxG0Xud1kpQZzic-Qfai0Fw6u9KPfiS7osHW4U_U5uWiWSYoX49axCuYNajbsAQbl4A"]

client = OpenAI(api_key=OPENAI_API_KEY)

SYSTEM_PROMPT = """
You are AI For All.
Reply in English unless the user asks for another language.
Be helpful, friendly, and accurate.
"""

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    response = client.responses.create(
        model="gpt-5.1-mini",
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
    )

    await update.message.reply_text(response.output_text)

app = Application.builder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

print("Bot started...")
app.run_polling()
