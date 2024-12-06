from enum import Enum as PyEnum

# 예약 상태 
class EReservationStatus(PyEnum):
    available = "판매중"
    reserved = "예약중"
    sold = "완료"

# 주문 상태
class EOrderStatus(PyEnum):
    in_progress = "거래 진행 중"
    completed = "거래 완료"
    awaiting_approval = "판매승인 대기"