from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Resep(Base):
    __tablename__ = "resep"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    judul = Column(String)
    bahan = Column(String)
    langkah = Column(String)
    kategori = Column(String)

    pemilik = relationship("User", back_populates="resep")