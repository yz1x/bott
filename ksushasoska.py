import telebot
import requests



bot = telebot.TeleBot("5474974340:AAG0sKGx5aeyggrsFnVqyWr4h_P4ZuvzULg")
a = " "
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Сәлем,мен Tiktok бағдарламасынан бейнені арнайы жазусыз жіберетін ботпын.')


@bot.message_handler(commands=['download'])
def download(message):
    bot.send_message(message.chat.id, 'Бейненін сілтемесін жіберіңіз:')


@bot.message_handler(content_types=['text'])
def upload(message):




    url = "https://tiktok-videos-without-watermark.p.rapidapi.com/getVideo"

    querystring = {"url": message.text}

    headers = {
        "X-RapidAPI-Key": "4c50034204msh20f51616c9bfcfcp14e446jsn5e6ae06f5279",
        "X-RapidAPI-Host": "tiktok-videos-without-watermark.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    be = response.text.find('wihout')
    ao = response.text.find('https://v', be)
    print(response.text[ao:ao+200])
    bot.send_document(message.chat.id,response.text[ao:ao+200])
  #  bot.send_message(message.chat.id, response.text)
   
    #a.encode = urllib.request.urlretrieve(url, destination)
    #bot.send_document(message.chat.id ,a)

    #bot.send_message(message.chat.id , url)


# @bot.message_handler(content_types=['text'])
# def url_checker(message):
# get = requests.get(message.text)

# if get.status_code == 200:
#    bot.send_message(message.chat.id, "Подождите..")
# else:
#   bot.send_message(message.chat.id, "Вы ввели не правильную ссылку или написали что-то другое")


# bot.reply_to(message, message.text)
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# bot.reply_to(message, message.text)
# @bot.message_handler(func=lambda message : message.text == '')

bot.polling()
