from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from .forms import UserRegisterForm



# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

"""
def user_check(user):
    post = user.get_object()
    if user.username==post.auther:
        return True
    return False
    @user_passes_test(user_check)
"""
def user_check(user):
    return user.objects.contains(auth.user)



@login_required
def profile(request):
    user_data = User.objects.get(username=request.user.username)
    user_posts = user_data.post_set.all()
    return render(request, 'users/profile.html', {'user_posts':user_posts})

@login_required
def user_profile(request, pk):
    user_data = User.objects.get(pk=pk)
    user_posts = user_data.post_set.all()
    return render(request, 'users/profile.html', {'user_posts':user_posts})