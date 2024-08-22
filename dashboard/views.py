from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login")
def dashboard(request):
    response = render(request, 'dashboard.html',)
    response.status_code = 200
    return response


# @login_required(login_url="/login")
def taskList(request):
    return render(request, 'list.html')