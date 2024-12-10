from typing import List
from pydantic import BaseModel

# Article inside UserDisplay
class Article(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    class Config:
        from_attributes = True

class UserBase(BaseModel):
    username: str
    email: str
    password: str
    class Config:
        from_attributes = True

class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article] = []
    class Config:
        from_attributes = True

# User inside ArticleDisplay
class User(BaseModel):
    id: int
    username: str
    email: str
    class Config:
        from_attributes = True

class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int
    class Config:
        from_attributes = True

class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User
    class Config:
        from_attributes = True