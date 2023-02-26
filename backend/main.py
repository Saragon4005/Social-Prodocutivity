from random import randint
import firebase_admin
from fastapi import FastAPI
from firebase_admin import credentials, db

app = FastAPI()

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


@app.put("bet")
def create_task(owned: str, task: str, deadline: int, betAmount: int, proof: str):
    ID = randint(100000, 999999)

    db.reference(f"bets/{ID}").set({
        "task": task,
        "betAmount": betAmount,
        "deadline": deadline,
        "completed": False,
        "creatorId": ID,
        "owned": owned,
        "proof": proof,
    })
