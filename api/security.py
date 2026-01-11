# Step 3 — Create Security Layer
from fastapi import Header, HTTPException
from api.firebase import verify_token

def get_firebase_user(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing Authorization header")

    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid Authorization format")

    token = authorization.replace("Bearer ", "")

    try:
        decoded = verify_token(token)
        return decoded
    except:
        raise HTTPException(status_code=401, detail="Invalid Firebase token")
