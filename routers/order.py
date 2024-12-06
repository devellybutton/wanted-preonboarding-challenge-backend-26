from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_orders():
    return {"message": "This is the orders endpoint"}