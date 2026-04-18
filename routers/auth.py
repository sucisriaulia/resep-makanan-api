from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.user import User
from schemas.user import UserCreate, UserResponse
from auth.jwt import hash_password, verify_password, create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/register", response_model=UserResponse, status_code=201)
def register(user: UserCreate, db: Session = Depends(get_db)):
    cek_user = db.query(User).filter(User.username == user.username).first()
    if cek_user:
        raise HTTPException(status_code=400, detail="Username sudah digunakan")
    user_baru = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password)
    )
    db.add(user_baru)
    db.commit()
    db.refresh(user_baru)
    return user_baru

@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Username atau password salah")
    token = create_access_token(data={"sub": db_user.username})
    return {"access_token": token, "token_type": "bearer"}