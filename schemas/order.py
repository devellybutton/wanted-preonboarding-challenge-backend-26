from pydantic import BaseModel
from datetime import datetime
from .enum import EOrderStatus

class Order(BaseModel):
    id: int  # 주문 ID 
    buyer_id: int  # 구매자 ID
    seller_id: int  # 판매자 ID
    product_id: int  # 제품 ID
    status: EOrderStatus  # 주문 상태 
    amount: float  # 총 주문 금액
    quantity: int  # 구매 수량
    transaction_date: datetime = None  # 거래일자
    created_at: datetime  # 생성일 
    updated_at: datetime = None  # 수정일 

    class Config:
        orm_mode = True
        anystr_strip_whitespace = True