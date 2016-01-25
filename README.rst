=============================
django-telegram-bot-demo
=============================

Django app demo using django-telegram-bot app. This demo follows Polls app described in Django tutorial.
Same actions over polls by web app can be done with the Telegram bot.

* List questions
* List choices of questions
* Vote for a choice


Installation
-------------------------------------

The repo is setup for heroku but.So you only need to clone it, create heroku app and push it. 
Also you need to set one enviroment variable for Telegram token: **TELEGRAM_BOT_TOKEN**

To get that token you need to create a Telegram bot https://core.telegram.org/bots.

When you have your django-app installed migrate DB::

	$ python manage.py migrate
	
Create superuser to create questions and choices in admin and play::

	$ python manage.py createsuperuser
	
**NOTE**: You can test it locally with settings_local or using django-telegram-bot tasks but this demo uses
the webhook and telegram requires secure connection and ssl.
https://core.telegram.org/bots/api#getting-updates

Web VS Telegram Bot
----------------------------------------------------------

Some screenshots comparing web app and telegram bot:

* Polls

.. image:: https://raw.github.com/jlmadurga/django-telegram-bot-demo/master/imgs/web_polls.png

.. image:: https://raw.github.com/jlmadurga/django-telegram-bot-demo/master/imgs/start_and_questions.png

* Choices and vote

.. image:: https://raw.github.com/jlmadurga/django-telegram-bot-demo/master/imgs/web_choices.png

.. image:: https://raw.github.com/jlmadurga/django-telegram-bot-demo/master/imgs/bot_choices_and_vote.png

* Vote results

.. image:: https://raw.github.com/jlmadurga/django-telegram-bot-demo/master/imgs/web_results.png

.. image:: https://raw.github.com/jlmadurga/django-telegram-bot-demo/master/imgs/bot_results.png

* Bot unknown command and help

.. image:: https://raw.github.com/jlmadurga/django-telegram-bot-demo/master/imgs/bot_unknown_and_help.png



You can check it using already created bot https://telegram.me/djangotelegrambotdemo_bot and the web app
with the demo already installed https://django-telegram-bot-demo.herokuapp.com/polls/


 

