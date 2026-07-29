from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["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"])

SYSTEM_PROMPT = """
You are Ethio AI, a helpful and intelligent AI assistant.

Rules:
- Reply in Afaan Oromoo by default.
- If the user writes in English, reply in English.
- If the user writes in Amharic, reply in Amharic.
- Be accurate, respectful, and concise.
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

app = Application.builder().token(os.environ["8829904176:AAFsSJGmRtmrIJJUSUld5FnQ-5f924TeqX0"]).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

print("Ethio AI Bot is running...")
app.run_polling()
