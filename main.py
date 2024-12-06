from fastapi import FastAPI
from database import engine
from models import Base
from routers import order_router, product_router, user_router

# 데이터베이스 모델 생성
Base.metadata.create_all(bind=engine)

app = FastAPI()

# 라우터 등록
app.include_router(order_router, prefix="/orders", tags=["orders"])
app.include_router(product_router, prefix="/products", tags=["products"])
app.include_router(user_router, prefix="/users", tags=["users"])