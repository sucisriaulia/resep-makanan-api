from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.user import User
from schemas.user import UserCreate, UserResponse
from typing import List

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/", response_model=UserResponse, status_code=201)
def buat_user(user: UserCreate, db: Session = Depends(get_db)):
    user_baru = User(
        username=user.username,
        email=user.email,
        password=user.password
    )
    db.add(user_baru)
    db.commit()
    db.refresh(user_baru)
    return user_baru

@router.get("/", response_model=List[UserResponse])
def lihat_semua_user(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.get("/{user_id}", response_model=UserResponse)
def lihat_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")
    return user

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_update: UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")
    for key, value in user_update.dict().items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user

@router.delete("/{user_id}")
def hapus_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")
    db.delete(user)
    db.commit()
    return {"message": "User berhasil dihapus"}