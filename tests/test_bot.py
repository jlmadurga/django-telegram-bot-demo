#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.test import TestCase
from telegrambot.models import Update, User, Chat
from django.core.urlresolvers import reverse
from rest_framework import status
from telegram.replykeyboardhide import ReplyKeyboardHide
from telegrambot.test import testcases, factories
from django.core.management import call_command
from django.utils.six import StringIO
from django.core.management.base import CommandError
from django.conf import settings
from django.apps import apps
try:
    from unittest import mock
except ImportError:
    import mock  # noqa
    
ModelUser = apps.get_model(getattr(settings, 'AUTH_USER_MODEL', 'auth.User'))

class TestBotPolls(testcases.BaseTestBot):
    fixtures = ['tests/fixtures/polls.json']
    
    start = {'in': '/start',
             'out': {'parse_mode': 'Markdown',
                     'reply_markup': '',
                     'text': "Wellcome to **django telegram bot demo**"
                     }
             }
    
    unknown = {'in': '/no_defined',
               'out': {'parse_mode': 'Markdown',
                       'reply_markup': '',
                       'text': "Unknown command please type /help to see commands"
                       }
               }
    
    help = {'in': '/help',
             'out': {'parse_mode': 'Markdown',
                     'reply_markup': '',
                     'text': "Commands:"
                     }
             }
    
    question_list = {'in': '/question',
                     'out': {'parse_mode': 'Markdown',
                             'reply_markup': '/question 1',
                             'text': "Select from list:"
                     }
             }
    
    question_detail = {'in': '/question 1',
                       'out': {'parse_mode': 'Markdown',
                               'reply_markup': '/vote 1',
                               'text': "Beach or Mountain"
                     }
             }
    
    vote_authed = {'in': '/vote 1',
                   'out': {'parse_mode': 'Markdown',
                           'reply_markup': '',
                           'text': "Mountain please -- 3 votes"
                           }
                   }
    
    vote_not_authed = {'in': '/vote 1',
                       'out': {'parse_mode': 'Markdown',
                               'reply_markup': '',
                               'text': "You need an *authenticated chat*" +
                                        " to perform this action please login" +
                                        " [here](https://example.com/telegrambot/auth/"
                               }
                       }
    
    def test_start(self):
        self._test_message_ok(self.start)
        
    def test_unknown(self):
        self._test_message_ok(self.unknown)
        
    def test_help(self):
        self._test_message_ok(self.help)
        
    def test_question_list(self):
        self._test_message_ok(self.question_list)
        
    def test_question_detail(self):
        self._test_message_ok(self.question_detail)
        
    def test_vote_already_authed(self):
        token = factories.AuthTokenFactory()
        token.save()
        chat, _ = Chat.objects.get_or_create(**self.update.message.chat.to_dict())
        token.chat_api = chat
        token.save()
        self._test_message_ok(self.vote_authed)
        
    def test_vote_not_authed(self):
        self._test_message_ok(self.vote_not_authed)