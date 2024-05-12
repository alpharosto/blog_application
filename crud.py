# crud.py

from bson import ObjectId
from db import posts_collection, comments_collection, likes_dislikes_collection  # Importing modules from the absolute path
from models import Post, Comment, LikeDislike  # Importing modules from the absolute path

class PostCRUD:
    @staticmethod
    def create_post(post: Post):
        return posts_collection.insert_one(post.dict())

    @staticmethod
    def get_post(post_id: str):
        return posts_collection.find_one({"_id": ObjectId(post_id)})

    @staticmethod
    def update_post(post_id: str, post_data: dict):
        return posts_collection.update_one({"_id": ObjectId(post_id)}, {"$set": post_data})

    @staticmethod
    def delete_post(post_id: str):
        return posts_collection.delete_one({"_id": ObjectId(post_id)})
    
class CommentCRUD:
    @staticmethod
    def create_comment(comment: Comment):
        return comments_collection.insert_one(comment.dict())

    @staticmethod
    def get_comment(comment_id: str):
        return comments_collection.find_one({"_id": ObjectId(comment_id)})

    @staticmethod
    def update_comment(comment_id: str, comment_data: dict):
        return comments_collection.update_one({"_id": ObjectId(comment_id)}, {"$set": comment_data})

    @staticmethod
    def delete_comment(comment_id: str):
        return comments_collection.delete_one({"_id": ObjectId(comment_id)})

class LikeDislikeCRUD:
    @staticmethod
    def create_like_dislike(like_dislike: LikeDislike):
        return likes_dislikes_collection.insert_one(like_dislike.dict())

    @staticmethod
    def get_like_dislike(like_dislike_id: str):
        return likes_dislikes_collection.find_one({"_id": ObjectId(like_dislike_id)})

    @staticmethod
    def update_like_dislike(like_dislike_id: str, like_dislike_data: dict):
        return likes_dislikes_collection.update_one({"_id": ObjectId(like_dislike_id)}, {"$set": like_dislike_data})

    @staticmethod
    def delete_like_dislike(like_dislike_id: str):
        return likes_dislikes_collection.delete_one({"_id": ObjectId(like_dislike_id)})
