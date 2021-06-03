from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList
from .forms import TodoForm
from django.utils import timezone
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='loginpage')
def homepage(request):
    todos = TodoList.objects.filter(user=request.user)
    context = {'todos': todos}
    return render(request, 'homepage.html', context)


@login_required(login_url='loginpage')
def addtodo(request):
    if request.method == 'GET':
        return render(request, 'homepage.html')
    else:
        title = request.POST.get('title')
        if title == '':
            return redirect('homepage')
        else:
            newtodo = TodoList(title=title)
            newtodo.user = request.user
            newtodo.save()
            message = messages.success(request, 'Todo Has Been Added!')
            return redirect('homepage')


@login_required(login_url='loginpage')
def completedtodo(request, list_id):
    todo = get_object_or_404(TodoList, pk=list_id, user=request.user)
    todo.is_done = True
    todo.save()
    return redirect('homepage')


@login_required(login_url='loginpage')
def uncompletedtodo(request, list_id):
    todo = get_object_or_404(TodoList, pk=list_id, user=request.user)
    todo.is_done = False
    todo.save()
    return redirect('homepage')


@login_required(login_url='loginpage')
def viewtodo(request, list_id):
    todo = get_object_or_404(TodoList, pk=list_id, user=request.user)
    context = {'todo': todo}
    return render(request, 'viewtodo.html', context)


@login_required(login_url='loginpage')
def updatetodo(request, list_id):
    todo = get_object_or_404(TodoList, pk=list_id, user=request.user)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo.created = timezone.now()
            form.save()
            message = messages.success(request, 'Todo Has Been Updated!')
            return redirect('homepage')
    context = {'form': form}
    return render(request, 'updatetodo.html', context)


@login_required(login_url='loginpage')
def deletetodo(request, list_id):
    todo = get_object_or_404(TodoList, pk=list_id, user=request.user)
    todo.delete()
    message = messages.error(request, 'Todo Has Been Deleted!')
    return redirect('homepage')


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                message = messages.error(
                    request, 'Username or Password is incorrect')
        return render(request, 'loginpage.html')


def signuppage(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                message = messages.success(
                    request, 'Congarts. Account created successfully!')
                return redirect('loginpage')
        context = {'form': form}
        return render(request, 'signuppage.html', context)


def logoutuser(request):
    logout(request)
    return redirect('loginpage')
