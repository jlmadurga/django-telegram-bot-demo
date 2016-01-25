from telegrambot.generic import TemplateCommandView, ListDetailCommandView, ListCommandView, DetailCommandView
from polls.models import Question, Choice

class StartCommandView(TemplateCommandView):
    template_code = "start"
    
class HelpCommandView(TemplateCommandView):
    template_code = "help"
    
class UnknownCommandView(TemplateCommandView):
    template_code = "unknown"    

class QuestionListCommandView(ListCommandView):
    template_code = "question_list"
    context_object_name = "questions"
    model = Question
    
class QuestionDetailCommandView(DetailCommandView):
    template_code = "question_detail"
    context_object_name = "question"
    model = Question
    slug_field = "id"

class QuestionCommandView(ListDetailCommandView):
    list_view_class = QuestionListCommandView
    detail_view_class = QuestionDetailCommandView
    
class VoteCommandView(TemplateCommandView):
    template_code = "vote"
    context_object_name = "question"
    
    def get_context(self, update):
        choice_id = update.message.text.split(' ')[1]
        selected_choice = Choice.objects.get(pk=choice_id)
        selected_choice.votes += 1
        selected_choice.save()
        context = {self.context_object_name : selected_choice.question}
        return context 