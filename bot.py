import os
from telebot.types import Message
from telebot import TeleBot
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = TeleBot(token=BOT_TOKEN)


@bot.message_handler(func=lambda message: True, chat_types=['supergroup'])
def channels_ban(updates: Message):
    if updates.sender_chat:
        bot.delete_message(
            chat_id=updates.chat.id,
            message_id=updates.message_id
        )
        bot.ban_chat_sender_chat(
            chat_id=updates.chat.id,
            sender_chat_id=updates.sender_chat.id
        )


@bot.message_handler(commands=["start"], chat_types=['private'])
def start_message(updates: Message):
    bot.send_message(
        updates.chat.id,
        f'Hello, [{updates.from_user.first_name}](tg://user?id={updates.from_user.id})\n\n'
        f'This is a telegram bot. It does not allow channels to send messages to the telegram supergroup.\n\n'
        f'Contact [Abhijith N T](tg://user?id=429320566) if you have any problems or create a '
        f'[new issue](https://github.com/AbhijithNT/GroupChannelHandler/issues/new) on GitHub',
        parse_mode='Markdown'
    )


bot.infinity_polling()
