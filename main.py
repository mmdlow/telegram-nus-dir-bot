import telebot
import telebot.types as types
import time

acad_links = {
'CORS': 'http://www.cors.nus.edu.sg/',
'EduRec': 'https://myisis.nus.edu.sg/psp/cs90prd/?cmd=login',
'IVLE': 'https://ivle.nus.edu.sg/default.aspx',
'LumiNus': 'https://luminus.nus.edu.sg/',
'NUS Libraries': 'https://libportal.nus.edu.sg/frontend/index',
'Nusmods': 'https://nusmods.com/'
}

faci_links = {}
facu_links = {}
resd_links = {}
misc_links = {}

link_dict = {
'academic': acad_links,
'facilities': faci_links,
'faculties': facu_links,
'residences': resd_links,
'miscellaneous': misc_links
}

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
	
	markup.row(types.InlineKeyboardButton('Academic', callback_data = 'academic'))
	markup.row(types.InlineKeyboardButton('Facilities', callback_data = 'facilities'))
	markup.row(types.InlineKeyboardButton('Faculties', callback_data = 'faculties'))
	markup.row(types.InlineKeyboardButton('Residences', callback_data = 'residences'))
	markup.row(types.InlineKeyboardButton('Miscellaneous', callback_data = 'miscellaneous'))

	bot.send_message(msg.chat.id, 
		'Hello! Welcome to the NUS Unified Online Directory :)\n\nTo begin, select a category:',
		reply_markup = markup)

# Handle inline queries from /start command (5 main categories only))
@bot.callback_query_handler(func = lambda call: call.data in link_dict.keys())
def start_callback(call):
	print('User selected ' + call.data + ' category')

	markup = types.InlineKeyboardMarkup()
	category = link_dict[call.data]
	for key in category.keys():
		markup.row(types.InlineKeyboardButton(key, url = category[key]))

	bot.answer_callback_query(call.id)
	bot.send_message(call.message.chat.id, f'You selected the {call.data} category.\n\nNext, choose a subcategory:',
		reply_markup = markup)

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