from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
import logging
from .models import News, User  # Assuming MongoDB models for news and users

logger = logging.getLogger(__name__)

class AdminDashboardView(View):
    def get(self, request):
        total_news = News.objects.count()
        total_users = User.objects.count()
        sentiment_counts = News.objects.aggregate([
            {"$group": {"_id": "$sentiment", "count": {"$sum": 1}}}
        ])
        return render(request, 'admin_dashboard.html', {
            "total_news": total_news,
            "total_users": total_users,
            "sentiment_counts": sentiment_counts
        })

class AdminNewsView(View):
    def get(self, request):
        news_list = News.objects.all()
        return render(request, 'admin_news.html', {"news_list": news_list})

class AdminUsersView(View):
    def get(self, request):
        users_list = User.objects.all()
        return render(request, 'admin_users.html', {"users_list": users_list})

def login_view(request):
    logger.debug("Trying to render template: login.html")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')  # Redirect to admin dashboard
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('login')
