from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', login_required(views.PostListView.as_view()), name='list'),
    path('post/', login_required(views.PostingView.as_view()), name='posting'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='detail'),
]
