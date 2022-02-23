from django.template import loader
from django.views.generic import TemplateView
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render,get_object_or_404
from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'easy_votings/index.html', context)

# Show specific question and choices


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'easy_votings/details.html', {'question': question})

# Get question and display results


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'easy_votings/results.html', {'question': question})

# Vote for a question choice


def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'easy_votings/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(question.id,)))

def about(request):
    return render(request,'easy_votings/aboud.html')

def sign(request):
    return render(request,'easy_votings/register.html')

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
    ##return redirect('index', permanent = False)

class RegisterUser():
    form_class = UserCreationForm
    template_name = 'easy_votings/register.html'
    success_url = reverse_lazy('login')
class ProfilePage(TemplateView):
    template_name = "registration/profile.html"
class RegisterView(TemplateView):
    template_name = "registration/register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                User.objects.create_user(username, email, password)
                return redirect(reverse("login"))

        return render(request, self.template_name)
class LoginView(TemplateView):
    template_name = "registration/login.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context)
