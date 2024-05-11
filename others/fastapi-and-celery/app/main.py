from fastapi import FastAPI
from fastapi import BackgroundTasks


app = FastAPI()

def send_email(email, message):
    pass 


@app.get("/")
async def ping(background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, "email@address.com", "Hi!")
    return {"message": "pong!"}