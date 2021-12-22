import os

from telebot import TeleBot
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = TeleBot(token=BOT_TOKEN)


@bot.message_handler(func=lambda message: True, chat_types=['supergroup'])
def channels_ban(message):
    if message.sender_chat:
        bot.delete_message(
            chat_id=message.chat.id,
            message_id=message.message_id
        )
        bot.ban_chat_sender_chat(
            chat_id=message.chat.id,
            sender_chat_id=message.sender_chat.id
        )


bot.infinity_polling()
