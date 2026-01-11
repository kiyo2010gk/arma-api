from fastapi import APIRouter, Depends
from api.security import get_firebase_user
from api.firebase import db

router = APIRouter(
    prefix="/products",
    dependencies=[Depends(get_firebase_user)],
    tags=["Products"]
)

@router.get("/")
def get_products():
    """Fetch products from Firestore"""
    products = []
    docs = db.collection("products").stream()
    for doc in docs:
        products.append(doc.to_dict())
    return products

@router.get("/inventory")
def get_inventory():
    """Fetch inventory from Firestore"""
    # Assuming inventory is also in Firestore, perhaps in a separate collection or same
    # The requirement said to use db.collection("products").stream() "anywhere data is fetched"
    # but logically inventory might be different. However, following the instruction literally:
    inventory = []
    docs = db.collection("inventory").stream()
    for doc in docs:
        inventory.append(doc.to_dict())
    return inventory
