import telebot as tg

from modules.weather import weather_report

with open('database/token.txt', encoding='utf8') as file:
    token = file.readline()
    file.close()

    bot = tg.TeleBot(token)
    
@bot.message_handler(commands=['start'], chat_types=['private'])
def start_function(message):
    bot.send_message(message.from_user.id, 'Bot for weather reports - Kaguya')

@bot.message_handler(commands=['weather'], chat_types=['private'])
def weather_function(message):
    context_message = bot.send_message(message.from_user.id, 'Type a city for reporting weather')
    bot.register_next_step_handler(context_message, weather_report_function)

def weather_report_function(message):
    language = 'en'
    city = message.text

    report = weather_report(city, language)

    bot.send_message(message.chat.id, report)

bot.polling(non_stop=True)
