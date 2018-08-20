'use strict';

const Telegram = require('telegram-node-bot');

class StartController extends Telegram.TelegramBaseController {
	startHandler($) {
		$.runInlineMenu({
			layout: 2,
			method: 'sendMessage',
			params: ['Hello! Welcome to the NUS Online Directory :)\
				\n\nTo begin, select a category:'],
			menu: [
			{
				text: 'Academic',
				callback: (callbackQuery, message) => {
					console.log("Academic selected")
				}
			},
			{
				text: 'Facilities',
				callback: (callbackQuery, message) => {
					console.log("Facilities selected")
				}
			},
			{
				text: 'Faculties',
				callback: (callbackQuery, message) => {
					console.log("Faculties selected")
				}
			},
			{
				text: 'Residences',
				callback: (callbackQuery, message) => {
					console.log("Residences selected")
				}
			}]
		})
	}
	get routes() {
		return {
			'startCommand': 'startHandler'
		};
	}
}

module.exports = StartController;