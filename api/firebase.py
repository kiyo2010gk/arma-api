import json
import os
import firebase_admin
from firebase_admin import credentials, firestore, auth

# Load Firebase key from Railway environment variable
raw = os.environ.get("FIREBASE_KEY_JSON")

if not raw:
    raise RuntimeError("FIREBASE_KEY_JSON environment variable is missing")

cred = credentials.Certificate(json.loads(raw))

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()


def verify_token(id_token: str):
    return auth.verify_id_token(id_token)
