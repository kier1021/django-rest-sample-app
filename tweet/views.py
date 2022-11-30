from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tweet
from .serializers import TweetSerializer

class TweetListAPIView(APIView):

    def get(self, request, *args, **kwargs):
        tweets = Tweet.objects.filter(user = request.query_params.get('user_id'))
        serializer = TweetSerializer(tweets, many=True)
        return Response({'tweets': serializer.data}, status=status.HTTP_200_OK)

class TweetAPIView(APIView):
    
    def get(self, request, *args, **kwargs):
        try:
            tweet = Tweet.objects.get(id=request.query_params.get('tweet_id'))
            serializer = TweetSerializer(tweet)
            return Response({'tweet': serializer.data}, status=status.HTTP_200_OK)
        except Tweet.DoesNotExist:
            
            return Response({'error': 'Tweet does not exists'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        data = {
            'content': request.data.get('content'), 
            'user': request.data.get('user_id')
        }

        serializer = TweetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Successfully created tweet', 'tweet': serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        try:
            tweet = Tweet.objects.get(id=request.query_params.get('tweet_id'))
            tweet.delete()
            return Response({'message': 'Successfully deleted the tweet'}, status=status.HTTP_200_OK)
        except Tweet.DoesNotExist:
            return Response({'error': 'Tweet does not exists'}, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, *args, **kwargs):
        try:
            tweet = Tweet.objects.get(id=request.data.get('tweet_id'))
            tweet.content = request.data.get('content')
            tweet.save()
            return Response({'message': 'Successfully updated the tweet'}, status=status.HTTP_200_OK)
        except Tweet.DoesNotExist:
            return Response({'error': 'Tweet does not exists'}, status=status.HTTP_400_BAD_REQUEST)