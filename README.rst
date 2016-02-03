=============================
django-telegram-bot-demo
=============================

Django app demo using django-telegram-bot app. This demo follows Polls app described in Django tutorial.
Same actions over polls by web app can be done with the Telegram bot.

* List questions
* List choices of questions
* Vote for a choice only once you have authenticated chat. You need to register in the website and login when telegram
requires.


Installation
-------------------------------------

The repo is setup for heroku but.So you only need to clone it, create heroku app and push it. 

When you have your django-app installed migrate DB::

	$ python manage.py migrate
	
Create superuser to create questions and choices in admin and play::

	$ python manage.py createsuperuser
	
To get that token you need to create a Telegram bot https://core.telegram.org/bots. After creating a bot in Telegram Platform, 
create at least one bot with django admin. Token is the only required field. You may need to provided public key certificate 
for your server. https://core.telegram.org/bots/self-signed Heroku has https and ssl by default so it is a good option if 
you dont want to deal with that.
	
	
To set the webhook for telegram you need ``django.contrib.sites`` installed, ``SITE_ID`` configured in settings and
with it correct value in the DB.


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


 

