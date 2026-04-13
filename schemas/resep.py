from pydantic import BaseModel

class ResepCreate(BaseModel):
    judul: str
    bahan: str
    langkah: str
    kategori: str

class ResepResponse(BaseModel):
    id: int
    judul: str
    bahan: str
    langkah: str
    kategori: str
    user_id: int
    
    class Config:
        from_attributes = True