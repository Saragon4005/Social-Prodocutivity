import firebase_admin
from fastapi import FastAPI
from firebase_admin import credentials, db

app = FastAPI()

cred = credentials.Certificate("social-productivity-sak.json")
firebase_admin.initialize_app(cred, { "databaseURL": "https://social-productivity-378922-default-rtdb.firebaseio.com" })


# db = firebase_admin.firestore.client()
@app.get("/")
async def root():
    doc_ref = db.reference("notes")
    doc_ref.set({ "wefhwehi": "ewhfwefhi" })
    dates = db.reference("notes").get()
    # doc_ref = db.collection('users').document('new_user')
    # doc_ref.set({
    #     'name': 'John Doe',
    #     'email': 'johndoe@example.com',
    #     'phone': '+1234567890'
    # })
    # doc_ref = db.collection('users').document('new_user')
    # doc = doc_ref.get()

    return {"message": "Hello World", "data": dates}


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
