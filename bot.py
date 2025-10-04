import telebot
import random
from bot_logic import gen_sticker, gen_pass, gen_emodji
    

bot = telebot.TeleBot("Token")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "/sticker - рандомный стикер" \
    " /pass - рандомный пароль" \
    " /emodji - рандомный эмодзи" \
    " /heh - hehehehehe")
    bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEPfyBo4N__bIBHsTM7-YTLnVKs_5pUXAAChRYAAnst0VXYAr1wo3Br0zYE')
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет!")
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEPfw5o4NXhd6OYL3krZAXYsiEtx8g0owACYzoAAg5JuUiqScsQLr79OTYE')

@bot.message_handler(commands=['pass'])
def send_password(message):
    password = gen_pass(10)  
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")    

@bot.message_handler(commands=['emodji'])
def send_emodji(message):
    emodji = gen_emodji()
    bot.reply_to(message, f"Вот эмоджи': {emodji}")

@bot.message_handler(commands=['sticker'])
def send_sticker1(message):
    sticker_id = gen_sticker()
    bot.send_sticker(message.chat.id, sticker_id)

@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(commands=['yatta'])
def yatta(message):
    for i in range(20):
        bot.send_message(message.chat.id, 'YATTA')
    for i in range(5):
        sticker_id = ['CAACAgIAAxkBAAEPf7Fo4Pu18VXD4gFlraU3zt6lH7peXwACkB4AAireiUjaL6DT0Ho-QjYE', \
                    'CAACAgIAAxkBAAEPf7No4Pv3db2zp3s7z65ve_Kh0ZKw_AAC1CgAAq_reEglbe_q-il6uDYE', \
                    'CAACAgIAAxkBAAEPf7Vo4PwPYh3FiMiVVp2uDyQtoE0NAwAC_SoAAltZgUjTJozBcZrFqTYE']
        bot.send_sticker(message.chat.id, random.choice(sticker_id))

    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
bot.infinity_polling()
