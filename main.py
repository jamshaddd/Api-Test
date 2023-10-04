from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def index():
    return {"status":"200","image":"https://raw.githubusercontent.com/jamshaddd/Api-Test/main/uploads/Screenshot%202023-06-05%20115052.png"}