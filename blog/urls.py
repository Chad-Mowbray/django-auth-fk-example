from django.urls import path
from .views import ListPostsView, PostCreateView

urlpatterns = [
    path('', ListPostsView.as_view()),
    path('new/', PostCreateView.as_view())
]