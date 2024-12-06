from pydantic import BaseModel
from datetime import datetime
from .enum import EReservationStatus

class Product(BaseModel):
    id: int  # 상품 ID
    name: str  # 상품 이름
    price: float  # 상품 가격
    reservation_status: EReservationStatus  # 예약 상태
    quantity: int  # 제품 수량
    created_at: datetime  # 생성일 
    updated_at: datetime = None  # 수정일 

    class Config:
        orm_mode = True
        anystr_strip_whitespace = True