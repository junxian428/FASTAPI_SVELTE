import time
import threading 
import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/data-display")
def hello():
    random_number= random.randint(0,100)
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    print('API called at: ' + result)
    return {"time": result, "random_number": random_number}

  
#def print_hello():
    #while(True):
        #time.sleep(1)
        #print(random.randint(0, 100))
        #localtime = time.localtime()
        #result = time.strftime("%I:%M:%S %p", localtime)
        #print(result)


#t1 = threading.Thread(target=print_hello)  
#t1.start()

