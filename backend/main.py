from random import randint
import firebase_admin
from fastapi import FastAPI
from firebase_admin import credentials, db

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


cred = credentials.Certificate("social-productivity-sak.json")
firebase_admin.initialize_app(
    cred, {"databaseURL": "https://social-productivity-378922-default-rtdb.firebaseio.com"})

'''
# db = firebase_admin.firestore.client()
@app.get("/")
async def root():
    doc_ref = db.reference("notes")
    doc_ref.set({"wefhwehi": "ewhfwefhi"})
    dates = db.reference("notes").get()

    return {"message": "Hello World", "data": dates}


@app.put("group")
def create_group(name: str, creator_id: str):
    ID = randint(100000, 999999)

    db.reference(f"groups/{ID}").set()
'''


@app.put("/bet")
def create_bet(owned: str, task: str, deadline: int, betAmount: int, proof: str):
    ID = randint(100000, 999999)
    response = {
        "task": task,
        "betAmount": betAmount,
        "deadline": deadline,
        "completed": False,
        "creatorId": ID,
        "owned": owned,
        "proof": proof,
        "id": ID
    }
    db.reference(f"bets/{ID}").set(response)
    return (response)


@app.get("/bet/{bet_id}")
def get_bet(bet_id: int):
    return db.reference(f"bets/{bet_id}").get()


@app.put("/user")
def create_user(name: str):
    ID = randint(100000, 999999)
    response = {
        "name": name,
        "id": ID,
    }
    db.reference(f"users/{ID}").set(response)
    return (response)


@app.get("/user/{user_id}")
def get_user(user_id: int):
    return db.reference(f"users/{user_id}").get()
