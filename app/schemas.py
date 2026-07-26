from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional, Annotated
from pydantic import ConfigDict



class PostBase(BaseModel):
    title : str
    content : str
    published : bool = True

class UserOut(BaseModel):
    email : EmailStr
    id : int
    created_at : datetime

    class config:
        orm_mode = True

class PostCreate(PostBase):
    pass

class PostReturn(PostBase):
    pass
    id : int
    created_at : datetime
    user_id : int
    owner : UserOut
    
    class config:
        orm_mode = True

class PostVote(BaseModel):
    Post : PostReturn
    votes : int

    model_config = ConfigDict(from_attributes=True)

class UserCreate(BaseModel):
    email : EmailStr
    password : str



class UserLogin(BaseModel):
    email : EmailStr
    password : str

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[int] = None

class Votes(BaseModel):
    post_id : int
    dir: Annotated[int, Field(ge=0, le=1)]