from pymongo import MongoClient

client = MongoClient("mongodb+srv://alpha:12345@cluster0.ngen05o.mongodb.net/blog_database?retryWrites=true&w=majority&appName=Cluster0")
db = client["blog_database"]

posts_collection = db["posts"]
comments_collection = db["comments"]
likes_dislikes_collection = db["likes_dislikes"]
