import telebot

bot = telebot.TeleBot("1487416357:AAEP0eg_P1tkqkHE8U-qOiZkdFmYJELoB24")

@bot.message_handler(content_types=['text'])
def send_welcome(message):
	bot.send_message(message.chat.id, message.text)

bot.polling()