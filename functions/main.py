from firebase_functions import https_fn
from firebase_admin import initialize_app
from google.cloud import firestore

initialize_app()
db = firestore.Client()

@https_fn.on_request()
def api(req):
    docs = db.collection("test").stream()
    data = [d.to_dict() for d in docs]
    return {
        "status": "Firebase Python API running",
        "count": len(data),
        "data": data
    }
