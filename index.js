'use strict';

const Telegram = require('telegram-node-bot'),
	tg = new Telegram.Telegram('', {
		workers: 1
	});

const StartController = require('./controllers/start');
const OtherwiseController = require('./controllers/otherwise');

tg.router.when(new Telegram.TextCommand('/start', 'startCommand'), new StartController())
	.otherwise(new OtherwiseController());