from polls.commands_views import StartCommandView, UnknownCommandView, \
    QuestionCommandView, VoteCommandView, HelpCommandView

commandspatterns = [('start', StartCommandView.as_command_view()),
                    ('question', QuestionCommandView.as_command_view()),
                    ('vote', VoteCommandView.as_command_view()),
                    ('help', HelpCommandView.as_command_view()),
                    (None, UnknownCommandView.as_command_view())]