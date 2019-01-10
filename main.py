import os
import telebot
import telebot.types as types
import time
from directory import *

# ONLY USE TO LOOK FOR CALLBACK DATA AS A KEYWORD
# Recursively check if a particular keyword exists as a key nested somewhere in link_dict
# May return either a dict or a string value mapped to that key
# or '' if it doesn't exist ('' guaranteed to be an invalid key and should not exist)
def keyword_search(dictionary, word):

	# Future extension: refine for more nuanced word searching
	if word.lower() in list(map(lambda x: x.lower(), dictionary.keys())):
		return dictionary[word]

	for key in dictionary.keys():
		if (isinstance(dictionary[key], dict)):
			result = keyword_search(dictionary[key], word)
			if (result != ''):
				return result

	return ''


# Get bot token

# Get token from Heroku config var
token = os.environ.get('API_TOKEN')

# If running locally, get from secret.txt
if token is None:
	try:
		token_file = open('secret.txt', 'r')
		token = token_file.read()
		token_file.close()
	except Exception as e:
		print('Couldn\'nt get bot token: ' + e)

# Create TeleBot instance
bot = telebot.TeleBot(token = token)

# Handle /start command
@bot.message_handler(commands = ['start'])
def send_welcome(msg):

	markup = types.InlineKeyboardMarkup()

	for key in link_dict.keys():
		markup.row(types.InlineKeyboardButton(key, callback_data = key))

	bot.send_message(msg.chat.id, 
		'Hello! Welcome to the NUS Unified Online Directory :)\n\nTo begin, select a category:',
		reply_markup = markup)

# Handle /help command
@bot.message_handler(commands = ['help'])
def send_help(msg):
	bot.send_message(msg.chat.id,
		'How to use this bot:\n\n1. Enter /start to access the main directory with the categories:\nAcademic\nFacilities\nFaculties\nResidences\nMiscellaneous\n\n2. Select the appropriate option to access either a link to the desired webpage or another subcategory')

# Handle all inline queries
@bot.callback_query_handler(func = lambda call: True)
def handle_callback(call):
	bot.answer_callback_query(call.id)

	# Search for call.data as a keyword nested somewhere in link_dict
	result = keyword_search(link_dict, call.data)

	# If cannot find keyword, send default message
	if (result == ''):
		send_default(call.message)
		return

	print('User selected ' + call.data + ' category')
	markup = types.InlineKeyboardMarkup()
	category = result

	# For now assume that category is guaranteed to be a dict
	for key in category.keys():
		# String value mapped to current key should indicate a url
		if (isinstance(category[key], str)):
			markup.row(types.InlineKeyboardButton(key, url = category[key]))

		# Dict value indicates another layer of subcategories
		elif (isinstance(category[key], dict)):
			markup.row(types.InlineKeyboardButton(key, callback_data = key))

	bot.send_message(call.message.chat.id, f'You selected the {call.data} category.\n\nNext, choose a subcategory:',
		reply_markup = markup)

# # Handle direct text search queries
# # User sends messages without any '/'-prefixed commands, e.g. 'Cors'
# # Acad only
# @bot.message_handler(func = lambda msg: True)
# def handle_direct_search(msg):
# 	return 

# Handle all other messages
@bot.message_handler(func = lambda msg: True)
def send_default(msg):
	bot.send_message(msg.chat.id, 'Sorry, I didn\'t quite get that')

# Run the bot
try:
	bot.polling(none_stop = True)
except Exception as e:
	# Bot sleeps for 15 seconds in case of error
	print(e)
	time.sleep(15)