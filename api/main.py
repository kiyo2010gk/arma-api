from fastapi import FastAPI
from api.routes import products

app = FastAPI(title="READ-ONLY ERP MIRROR")

app.include_router(products.router)

@app.get("/")
def health_check():
    return {"status": "mirror_online", "source": "shadow_erp/"}
