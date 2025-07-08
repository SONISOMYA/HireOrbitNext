from pydantic import BaseModel , EmailStr

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class JobCreate(BaseModel):
    company: str
    position: str
    status: str

class UserCreate(BaseModel):
    username: str
    email: EmailStr  
    password: str

class JobOut(BaseModel):
    id: int
    company: str
    position: str
    status: str

    class Config:
        from_attributes = True