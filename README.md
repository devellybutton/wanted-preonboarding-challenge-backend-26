# Wanted Market API와 결제 프로세스 구축
#### - 원티드 프리온보딩 챌린지 백엔드 20, 26 사전과제

## 개발 과정
> 1. 프로젝트 세팅
> 2. 모델 생성 
> 3. API 명세
> 4. 서비스 코드 작성
> 5. 에러 처리
> 6. 테스트 코드 작성

### FastAPI를 선택한 이유
- 요구사항에 <b>python 이나 java 기반 프레임워크</b> 중 선택하라고 써있어서 그나마 익숙한 파이썬으로 선택함.
- <b>자동화된 API 문서화</b> : Swagger UI와 ReDoc을 자동으로 생성, API 명세서를 직접 작성하지 않아도 됨.
- <b>유효성 검사 및 타입 안정성</b> : Pydantic으로 자동 처리
- <b>비동기 요청 처리</b>를 기본적으로 지원
- <b>개발 속도 향상</b> : 코드가 간결하고 직관적이고 Django에 비해 설정이 간단함.
- <b>빠른 성능</b> : Starlette과 Uvicorn을 기반으로 하여 매우 빠른 성능


