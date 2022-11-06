

from django.shortcuts import render,redirect
from api.forms import RegistrationForm,QuestionForm,AnswerForm
from django.views.generic import TemplateView
from django.views.generic import CreateView,FormView,ListView,DetailView
from django.urls import reverse_lazy
from api.forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import render,redirect
from api.models import Questions,Answers
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache


from api.models import MyUser

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect('sigin')
        else:
            return fn(request,*args,**kwargs)
    return wrapper

decs=[signin_required,never_cache]

        
@method_decorator(decs,name="dispatch")
class IndexView(CreateView,ListView):
    template_name="home.html"
    form_class=QuestionForm
    model=Questions
    success_url=reverse_lazy('index')
    context_object_name="questions"

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        return Questions.objects.all().exclude(user=self.request.user)





class SignupView(CreateView):
    model=MyUser
    form_class=RegistrationForm
    template_name="register.html"
    success_url=reverse_lazy('register')
    


class LoginView(FormView):
    form_class=LoginForm
    template_name="login.html"


    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get('username')
            pwd=form.cleaned_data.get('password')
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"login success")
                return redirect('index')
            else:
                messages.error(request,"invalid activity")
                return render(request,"login.html",{"form":form})


# class MyQuestions(ListView):
#     model=Questions
#     template_name="myque"
#     success_url="home"
#     context_object_name='qlist'

#     def get_queryset(self):
#         return Questions.objcts.filter(user=self.request.user)


@method_decorator(decs,name="dispatch")
class QuestionDetailsView(DetailView,FormView):
    model=Questions
    template_name="question-detail.html"
    pk_url_kwarg="id"
    context_object_name="question"
    form_class=AnswerForm



decs
def add_ans(request,*args,**kwargs):

    if request.method=="POST":
        form=AnswerForm(request.POST)
        if form.is_valid():
            ans=form.cleaned_data.get("answer")
            qid=kwargs.get("id")
            ques=Questions.objects.get(id=qid)
            Answers.objects.create(qustion=ques,user=request.user,answer=ans)
            return redirect('index')
        else:
            return redirect('index')


decs
def upvote_view(request,*args,**kwargs):
    ansid=kwargs.get("id")
    ans=Answers.objects.get(id=ansid)
    ans.up_vote.add(request.user)
    ans.save()
    return redirect('index')

    


decs
def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("sigin")



decs
def remove_ans(request,*args,**kwargs):
    ans_id=kwargs.get("id")
    Answers.objects.get(id=ans_id).delete()
    return redirect('index')


