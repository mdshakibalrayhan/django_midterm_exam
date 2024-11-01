from django.contrib.auth.forms import AuthenticationForm
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.views.generic import CreateView,DetailView
from .forms import RegistraionForm
from .models import CarModel
from comments.forms import CommentForm
from comments.models import Comment
from author.models import CarOwner
from author.forms import CarOwnerForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import Update_User_Data
# Create your views here.

class login(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    def get_success_url(self):
        return reverse_lazy('homepage')

def logout_trigger(request):
    logout(request)
    return redirect('login')

def logoutpage(request):
    return render(request,'logout.html')

class Registraion(CreateView):
    template_name = 'register.html'
    form_class = RegistraionForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)

@login_required    
def update_usuer_details(request,id):
    user = User.objects.get(pk=id)
    if request.method == 'POST':
        form = Update_User_Data(request.POST,instance=user)
        form.save()
        return redirect('profile',id=id)
    else:
        form = Update_User_Data(instance=user)
    return render(request,'change_data.html',{'form':form})


class PostDetailsView(DetailView):
    model = CarModel
    template_name = 'details.html'
    pk_url_kwarg = 'id'

    def post(self,request,*args,**kwargs):
        comment_for = self.get_object()
        comment_form = CommentForm(data=self.request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.comment_for = comment_for
            new_comment.save()
            return redirect('details',id=comment_for.id)
        return self.get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        data = self.get_object()
        comment_for = self.get_object()
        comments = Comment.objects.filter(comment_for = comment_for.id)
        comment_form = CommentForm()
        context['data'] = data
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

@login_required
def edit_quantity_after_purchase(request,id):
    data = CarModel.objects.filter(id=id)
    carowner = CarOwner()
    
    
    for d in data:
        d.quantity = d.quantity - 1
        d.save()
        carowner.owned_car = d.model_name
    
    carowner.owner = User.objects.get(id=request.user.id)

    carowner.save()
    
    
    return redirect('details',id)