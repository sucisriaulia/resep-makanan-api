from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.resep import Resep
from schemas.resep import ResepCreate, ResepResponse
from typing import List

router = APIRouter(
    prefix="/resep",
    tags=["resep"]
)

@router.post("/", response_model=ResepResponse, status_code=201)
def buat_resep(resep: ResepCreate, db: Session = Depends(get_db)):
    resep_baru = Resep(**resep.dict(), user_id=1)
    db.add(resep_baru)
    db.commit()
    db.refresh(resep_baru)
    return resep_baru

@router.get("/", response_model=List[ResepResponse])
def lihat_semua_resep(db: Session = Depends(get_db)):
    return db.query(Resep).all()

@router.get("/{resep_id}", response_model=ResepResponse)
def lihat_resep(resep_id: int, db: Session = Depends(get_db)):
    resep = db.query(Resep).filter(Resep.id == resep_id).first()
    if not resep:
        raise HTTPException(status_code=404, detail="Resep tidak ditemukan")
    return resep

@router.put("/{resep_id}", response_model=ResepResponse)
def update_resep(resep_id: int, resep_update: ResepCreate, db: Session = Depends(get_db)):
    resep = db.query(Resep).filter(Resep.id == resep_id).first()
    if not resep:
        raise HTTPException(status_code=404, detail="Resep tidak ditemukan")
    for key, value in resep_update.dict().items():
        setattr(resep, key, value)
    db.commit()
    db.refresh(resep)
    return resep

@router.delete("/{resep_id}")
def hapus_resep(resep_id: int, db: Session = Depends(get_db)):
    resep = db.query(Resep).filter(Resep.id == resep_id).first()
    if not resep:
        raise HTTPException(status_code=404, detail="Resep tidak ditemukan")
    db.delete(resep)
    db.commit()
    return {"message": "Resep berhasil dihapus"}