import telebot
import telebot.types as types
import time

# Get bot token
try:
	token_file = open('secret.txt', 'r')
	token = token_file.read()
	token_file.close()
except Exception:
	print('Couldn\'nt get bot token')

# Create TeleBot instance
bot = telebot.TeleBot(token = token)

# Handle /start command
@bot.message_handler(commands = ['start'])
def send_welcome(msg):

	markup = types.InlineKeyboardMarkup()
	academic = types.InlineKeyboardButton('Academic', callback_data = 'academic')
	facilities = types.InlineKeyboardButton('Facilities', callback_data = 'facilities')
	faculties = types.InlineKeyboardButton('Faculties', callback_data = 'faculties')
	residences = types.InlineKeyboardButton('Residences', callback_data = 'residences')
	
	markup.row(academic)
	markup.row(facilities)
	markup.row(faculties)
	markup.row(residences)

	bot.send_message(msg.chat.id, 
		'Hello! Welcome to the NUS Unified Online Directory :)\n\nTo begin, select a category:',
		reply_markup = markup)

# Handle inline queries from /start command
@bot.callback_query_handler(func = lambda call: True)
def start_callback(call):
	print('User selected ' + call.data + ' category')
	bot.answer_callback_query(call.id)
	bot.send_message(call.message.chat.id, f'You selected the {call.data} category.\n\nNext, choose a subcategory:')

# Handle all other messages
@bot.message_handler(func = lambda msg: True)
def send_default(msg):
	bot.send_message(msg.chat.id, 'Sorry, I didn\'t quite get that')

# Run the bot
while True:
	try:
		bot.polling()
	except Exception:
		# Bot sleeps for 15 seconds in case of error
		time.sleep(15)