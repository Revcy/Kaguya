import telebot as tg

from modules.weather import weather_report

with open('database/tokens.txt', encoding='utf8') as file:
    tokens = file.readlines()
    token, appid_openweathermap = tokens[0].replace('\n', ''), tokens[1].replace('\n', '')
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
    report = weather_report(city, language, appid_openweathermap)

    if report != None:
        weather_key = tg.types.InlineKeyboardMarkup(row_width=1)
        button = tg.types.InlineKeyboardButton(text='Detailed report', url=f'https://openweathermap.org/city/{report[9]}')
        weather_key.add(button)
        
        bot.send_message(message.chat.id, f'Weather info for {report[0]}, {report[1]}: \n\nTime: {report[2]} \nDescription: {report[3]} \nTemperature: {report[4]}°C (Feels like: {report[5]}°C) \nWing speed: {report[6]} m/s \nPressure: {report[7]} Pa \nHumidity: {report[8]}%', reply_markup=weather_key)

bot.polling(non_stop=True)
