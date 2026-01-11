import firebase_admin
from firebase_admin import credentials, auth, firestore
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
KEY_PATH = os.path.join(BASE_DIR, "firebase-key.json")

cred = credentials.Certificate(KEY_PATH)
firebase_admin.initialize_app(cred)

db = firestore.client()

def verify_token(id_token: str):
    return auth.verify_id_token(id_token)
