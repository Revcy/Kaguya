import telebot as tg

with open('database/token.txt', encoding='utf8') as file:
    token = file.readline(0)
    file.close()

    bot = tg.TeleBot(token=token)
    
@bot.message_handler(commands=['start'], chat_types=['private'])
def start_function(message):
    pass

bot.polling(non_stop=True)
