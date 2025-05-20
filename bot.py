# bot.py

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from predict_operator import predict_operator

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Send me a mobile number or a list of numbers (comma or newline separated), and I'll tell you the operator and circle."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    # Accept comma, newline, or space-separated numbers
    separators = [',', '\n', ' ']
    for sep in separators:
        text = text.replace(sep, '\n')  # Normalize to newline
    
    numbers = [num.strip() for num in text.split('\n') if num.strip() and num.strip().isdigit()]

    if not numbers:
        await update.message.reply_text("Please send valid mobile numbers only.")
        return

    response_lines = []
    for num in numbers:
        operator, circle = predict_operator(num)
        response_lines.append(f"{num} => Operator: {operator}, Circle: {circle}")

    response_text = "\n".join(response_lines)
    await update.message.reply_text(response_text)

if __name__ == "__main__":
    application = ApplicationBuilder().token("7824028069:AAERlam8M4ktTnUfzg3b0Tjx4vYlSKUqzyY").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()
