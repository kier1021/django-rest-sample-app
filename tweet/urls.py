from django.urls import path
from .views import (
    TweetListAPIView,
    TweetAPIView,
    TweetCreateAPIView,
    UserTweetsAPIView,
)


urlpatterns = [
    path('tweets', TweetListAPIView.as_view()),
    path('tweet', TweetCreateAPIView.as_view()),
    path('tweet/<int:tweet_id>', TweetAPIView.as_view()),
    path('tweets/user/<int:user_id>', UserTweetsAPIView.as_view())
]
