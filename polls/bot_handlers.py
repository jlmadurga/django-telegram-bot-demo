from polls.commands_views import StartCommandView, UnknownCommandView, \
    QuestionCommandView, VoteCommandView, HelpCommandView

from telegrambot.handlers import command, unknown_command

bothandlers = [command('start', StartCommandView.as_command_view()),
               command('question', QuestionCommandView.as_command_view()),
               command('vote', VoteCommandView.as_command_view()),
               command('help', HelpCommandView.as_command_view()),
               unknown_command(UnknownCommandView.as_command_view())]