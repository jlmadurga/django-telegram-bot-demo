from telegrambot.bot_views.generic import TemplateCommandView, ListDetailCommandView, ListCommandView, \
    DetailCommandView
from polls.models import Question, Choice

class StartCommandView(TemplateCommandView):
    template_text = "bot/messages/command_start_text.txt"
    
class HelpCommandView(TemplateCommandView):
    template_text = "bot/messages/command_help_text.txt"
    
class UnknownCommandView(TemplateCommandView):
    template_text = "bot/messages/command_unknown_text.txt"    

class QuestionListCommandView(ListCommandView):
    template_text = "bot/messages/command_question_list_text.txt"
    template_keyboard = "bot/messages/command_question_list_keyboard.txt"
    context_object_name = "questions"
    model = Question
    
class QuestionDetailCommandView(DetailCommandView):
    template_text = "bot/messages/command_question_detail_text.txt"
    template_keyboard = "bot/messages/command_question_detail_keyboard.txt"
    context_object_name = "question"
    model = Question
    slug_field = "id"

class QuestionCommandView(ListDetailCommandView):
    list_view_class = QuestionListCommandView
    detail_view_class = QuestionDetailCommandView
    
class VoteCommandView(TemplateCommandView):
    template_text = "bot/messages/command_vote_text.txt"
    context_object_name = "question"
    
    def get_context(self, bot, update, **kwargs):
        choice_id = update.message.text.split(' ')[1]
        selected_choice = Choice.objects.get(pk=choice_id)
        selected_choice.votes += 1
        selected_choice.save()
        context = {self.context_object_name : selected_choice.question}
        return context 