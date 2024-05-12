from pydantic import BaseModel

class Post(BaseModel):
    title: str
    content: str
    author: str

class Comment(BaseModel):
    post_id: str
    content: str
    author: str

class LikeDislike(BaseModel):
    post_id: str
    action: str  
    user: str