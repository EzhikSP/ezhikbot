# -*- coding: utf-8 -*-
import telebot

TOKEN = '300669839:AAHvtEhtTYeSXt811LTKoKy961Zs0G_Lr7s'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Меня зовут Джарвис")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, 'Я пока тупой и не могу ничего иного ответить...')

bot.polling()
