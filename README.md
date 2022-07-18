## Create the FastAPI Code

    Create an app directory and enter it.
    Create an empty file __init__.py.
    Create a main.py file with:


from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"get": "subscriptions"}


@app.get("/subscriptions/{subscription_id}")
def read_item(subscription_id: int, service: Union[str, None] = None):
    return {"subscription_id": subscription_id, "123": service}


# You should now have a directory structure like:
```
.
├── app
│   ├── __init__.py
│   └── main.py
├── Dockerfile
└── requirements.txt
```

## Dockerfile

Now in the same project directory create a file Dockerfile with:


FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]


# Behind a TLS Termination Proxy

If you are running your container behind a TLS Termination Proxy (load balancer) like Nginx or Traefik, add the option --proxy-headers, this will tell Uvicorn to trust the headers sent by that proxy telling it that the application is running behind HTTPS, etc.

CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]




$ docker build -t myfastapi .

$ docker run -d --name fastapi -p 80:80 myfastapi




## Check it

You should be able to check it in your Docker container's URL, for example: http://192.168.99.100/subscriptions/5012333226?service=PrepaidCharging or http://127.0.0.1/subscriptions/5012333226?service=PrepaidCharging (or equivalent, using your Docker host).

You will see response something like:

{
    123	"PrepaidCharging"
    subscription_id	5012333226
}

![alt text](https://github.com/EngMohamedElEmam/simple-api-docker/blob/master/fastapi-HTTP-request.jpg?raw=true)

## Interactive API docs

Now you can go to http://192.168.99.100/docs or http://127.0.0.1/docs (or equivalent, using your Docker host).

You will see the automatic interactive API documentation you can try excuting from it such as this : 
![alt text](https://github.com/EngMohamedElEmam/simple-api-docker/blob/master/fastapi-swagger.jpg?raw=true)


## Refernce 
[FastAPI documentation](https://fastapi.tiangolo.com/tutorial/getting-started/) for more information.
