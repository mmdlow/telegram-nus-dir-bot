'use strict';

const Telegram = require('telegram-node-bot'),
	tg = new Telegram.Telegram('646192473:AAEwD5ex1TFJpC0Dntani_wtmV5YThccxaw', {
		workers: 1
	});

const PingController = require('./controllers/ping');
const OtherwiseController = require('./controllers/otherwise');

tg.router.when(new Telegram.TextCommand('/ping', 'pingCommand'), new PingController())
	.otherwise(new OtherwiseController());