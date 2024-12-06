from pydantic import BaseModel
from datetime import datetime
from typing import List

class User(BaseModel):
    id: int  # 사용자 ID 
    username: str  # 사용자 이름
    email: str  # 사용자 이메일
    password: str  # 사용자 비밀번호
    created_at: datetime = None  # 생성일 
    deleted_at: datetime = None  # 삭제일 

    orders: List[int] = []  # 구매 내역 (주문 ID값)
    sales: List[int] = []  # 판매 내역 (상품 ID값)

    class Config:
        orm_mode = True
        anystr_strip_whitespace = True