from typing import Optional
from fastapi import FastAPI,Body,Depends,Query
from schemas import PassParam
import random

app = FastAPI()

@app.get("/ping/")
def view():
    return {"message":"pong"}


@app.get("/genpwd/")
def generate_password(pwd: PassParam = Depends()):
    """
    # Функция генерирует пароль по в
    ## Header 2
    ### Header 3
    - item
    - item
    - item
    some `code` and _some italic_
    Creates new item
    """
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    number = pwd.numbers
    length = pwd.length
    result = []
    for n in range(number):
        password =''
        for i in range(length):
            password += random.choice(chars)
        result.append(password)
        print(password)
    return {"passwords":result}