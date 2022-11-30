from django.urls import path, include
from .views import (
    TweetListAPIView,
    TweetAPIView,
)

urlpatterns = [
    path('tweets', TweetListAPIView.as_view()),
    path('tweet', TweetAPIView.as_view()),
]

