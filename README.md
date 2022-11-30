# django-rest-sample-app
Sample REST API application that uses django rest framework


## Init python virtual env and dependency
```
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
```

## Migrate and start the project
```
python manage.py migrate
python manage.py runserver
```


## REST API endpoints

### Tweet

Get list of tweet of user
```
GET http://127.0.0.1:8000/api/v1/tweets/user<int:user_id>
```

Get tweet by ID
```
GET http://127.0.0.1:8000/api/v1/tweet/<int:tweet_id>
```

Update tweet by ID
```
PUT http://127.0.0.1:8000/api/v1/tweet/<int:tweet_id>

Content-Type: application/json

{
    "tweet_id": 1,
    "content": "What's up guys!" 
}
```

Delete tweet by ID
```
DELETE http://127.0.0.1:8000/api/v1/tweet/<int:tweet_id>
```

Create Tweet
```
POST http://127.0.0.1:8000/api/v1/tweet

Content-Type: application/json

{
    "user_id": 1,
    "content": "What's up guys!" 
}
```

### User

Create User
```
POST http://127.0.0.1:8000/api/v1/user

Content-Type: application/json

{
    "first_name": "",
    "last_name": "",
    "email": "",
    "password": "",
    "username": ""
}
```