import telebot
import schedule
import threading
import time
token = "1672405577:AAH-CpWekEO-iClbuSbn8o9LcWGhxszj1mg"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])  
def start_command(message):  
    bot.send_message(  
        message.chat.id,  
        'Greetings! I can show you exchange rates.\n' +  
        'To get the exchange rates press /exchange.\n' +  
        'To get help press /help.'  
  )
userId = 0
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    userId = message.from_user.id
    print(userId)
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    elif message.text == "ShAmIl":
        bot.send_message(message.from_user.id, token)
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')

def ob():
    bot.send_message(926299776, "Hellow")

def send_napom():
    schedule.every().minutes.do(ob)
    while(True):
        schedule.run_pending()
        

thread = threading.Thread(target=send_napom)
thread.start()
bot.polling(none_stop=True)