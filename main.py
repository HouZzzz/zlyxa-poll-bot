import random
import os

import telebot

import answer_handler
import questions_container

# server for vercel
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}


token = os.environ.get('TOKEN')
bot = telebot.TeleBot(token)

usersAndSteps = {}

questions = questions_container.questions

@bot.message_handler()
def start(message):
	print("handling message with text: " + message.text)
	if message.text == '/start':
		response_options = telebot.types.InlineKeyboardMarkup(row_width=2)
		for i in questions_container.answers[0]:
			response_options.add(telebot.types.InlineKeyboardButton(i, callback_data=i))

		bot.send_message(message.chat.id,questions[0],parse_mode="html",reply_markup=response_options)
		usersAndSteps.update({message.chat.id : 0})

				# debug
	elif message.text == 'check':
		if (message.chat.id == 1016872254):
			text = ''
			for key in usersAndSteps.keys():
				text += f'{key} : {usersAndSteps[key]}\n'

			bot.send_message(message.chat.id,text)

	elif message.text == "/brawlstars":
		bot.send_message(message.chat.id,"вау, ты нашел пасхалку. возьми с полки пирожок и скажи этому челу (@H0uZz (создатель сия шедевра)), что нашел посхалочку🥰")
	elif message.text == 'пакеж результат':
		bot.send_message(message.chat.id,f'Ты ждешь валорант мобайл на {random.randint(0,200)}%',reply_markup=telebot.types.ReplyKeyboardRemove())

@bot.callback_query_handler(func=lambda call: True)
def answers(callback):
	print("handling callback with data: " + callback.data)
	
	if (callback.message.chat.id in usersAndSteps.keys()):
		emotion = answer_handler.handle_answer(callback.data,usersAndSteps[callback.message.chat.id])

		if emotion.split("|")[0] != "":
			bot.send_message(callback.message.chat.id, emotion.split("|")[0],parse_mode="html")

		# skip question
		if ("|" in emotion):
			usersAndSteps.update({callback.message.chat.id : usersAndSteps[callback.message.chat.id] + (int(emotion.split("|")[1]) + 1)})
		else:
			usersAndSteps.update({callback.message.chat.id : usersAndSteps[callback.message.chat.id] + 1})

		if (usersAndSteps[callback.message.chat.id] != len(questions) - 1):
			replies = telebot.types.InlineKeyboardMarkup(row_width=3)
			for i in questions_container.answers[usersAndSteps[callback.message.chat.id]]:
				replies.add(telebot.types.InlineKeyboardButton(i.lower(), callback_data=i))
		else:
			replies = telebot.types.ReplyKeyboardMarkup(row_width=2)
			btn1 = telebot.types.KeyboardButton('пакеж результат')
			replies.add(btn1)

		bot.send_message(callback.message.chat.id,questions[usersAndSteps[callback.message.chat.id]],parse_mode="html",reply_markup=replies)
	else:
		bot.send_message(callback.message.chat.id,"Тебя нету в списке людей, которые проходят опрос")

# start bot
bot.polling(none_stop=True)