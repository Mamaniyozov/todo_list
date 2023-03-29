from django.http import HttpResponse, JsonResponse,HttpRequest
from django.views import View
# Import user model
from django.contrib.auth.models import User
from .models import Task
# Import authentication classes
import json
from django.contrib.auth import authenticate
from base64 import b64decode

def isAuth(auth):
    if auth is None:
        return False
    # Get token
    token = auth.split(' ')[1]
    auth=b64decode(token).decode() # Decode token
    username, password = auth.split(':') # Split token

    # Check if user is authenticated
    
    user = authenticate(username=username, password=password)

    if user is not None:
        return user
    return False



def add(request: HttpRequest) -> JsonResponse:
    """
    Create a task
    """
    auth = request.headers.get('Authorization')
    if isAuth(auth):
        if request.method == 'POST':
            body = request.body
        # get body data
            decoded = body.decode()
            # data to dict
            data = json.loads(decoded)
            task=data.get("task",False)
            description=data.get("description",False)
            complited=data.get("complited",False)
            result=Task(
                task=task,
                description=description,
                complited=complited,
                student=isAuth(auth)


            )
            result.save()
            return JsonResponse ({"result": "ok"})

        
        
        
    else:
        return JsonResponse({'message': 'Unauthorized'}, status=401)

            



        