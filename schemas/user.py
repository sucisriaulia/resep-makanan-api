from pydantic import BaseModel

class userCreate(BaseModel):
    username: str
    email: str
    password: str

class userResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True  