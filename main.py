# main.py

from fastapi import FastAPI, HTTPException
from typing import List
from models import Post, Comment, LikeDislike  # Importing models from the absolute path
from crud import PostCRUD, CommentCRUD, LikeDislikeCRUD  # Importing CRUD operations from the absolute path

app = FastAPI()

# Routes for posts
@app.post("/posts/")
async def create_post(post: Post):
    return PostCRUD.create_post(post)

@app.get("/posts/{post_id}")
async def read_post(post_id: str):
    post = PostCRUD.get_post(post_id)
    if post:
        return post
    raise HTTPException(status_code=404, detail="Post not found")

@app.put("/posts/{post_id}")
async def update_post(post_id: str, post: Post):
    if PostCRUD.get_post(post_id):
        return PostCRUD.update_post(post_id, post.dict())
    raise HTTPException(status_code=404, detail="Post not found")

@app.delete("/posts/{post_id}")
async def delete_post(post_id: str):
    if PostCRUD.get_post(post_id):
        return PostCRUD.delete_post(post_id)
    raise HTTPException(status_code=404, detail="Post not found")

# Routes for comments
@app.post("/comments/")
async def create_comment(comment: Comment):
    return CommentCRUD.create_comment(comment)

@app.get("/comments/{comment_id}")
async def read_comment(comment_id: str):
    comment = CommentCRUD.get_comment(comment_id)
    if comment:
        return comment
    raise HTTPException(status_code=404, detail="Comment not found")

@app.put("/comments/{comment_id}")
async def update_comment(comment_id: str, comment: Comment):
    if CommentCRUD.get_comment(comment_id):
        return CommentCRUD.update_comment(comment_id, comment.dict())
    raise HTTPException(status_code=404, detail="Comment not found")

@app.delete("/comments/{comment_id}")
async def delete_comment(comment_id: str):
    if CommentCRUD.get_comment(comment_id):
        return CommentCRUD.delete_comment(comment_id)
    raise HTTPException(status_code=404, detail="Comment not found")

# Routes for likes/dislikes
@app.post("/likes-dislikes/")
async def create_like_dislike(like_dislike: LikeDislike):
    return LikeDislikeCRUD.create_like_dislike(like_dislike)

@app.get("/likes-dislikes/{like_dislike_id}")
async def read_like_dislike(like_dislike_id: str):
    like_dislike = LikeDislikeCRUD.get_like_dislike(like_dislike_id)
    if like_dislike:
        return like_dislike
    raise HTTPException(status_code=404, detail="Like/Dislike not found")

@app.put("/likes-dislikes/{like_dislike_id}")
async def update_like_dislike(like_dislike_id: str, like_dislike: LikeDislike):
    if LikeDislikeCRUD.get_like_dislike(like_dislike_id):
        return LikeDislikeCRUD.update_like_dislike(like_dislike_id, like_dislike.dict())
    raise HTTPException(status_code=404, detail="Like/Dislike not found")

@app.delete("/likes-dislikes/{like_dislike_id}")
async def delete_like_dislike(like_dislike_id: str):
    if LikeDislikeCRUD.get_like_dislike(like_dislike_id):
        return LikeDislikeCRUD.delete_like_dislike(like_dislike_id)
    raise HTTPException(status_code=404, detail="Like/Dislike not found")
