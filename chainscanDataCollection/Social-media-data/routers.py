from fastapi import APIRouter, Depends, HTTPException
from Scripts.schemas import AnalysisResponse, UserCreate
from Scripts.schemas import PostCreate
from Scripts.database import AsyncSessionLocal
from Scripts.auth import get_current_user
from Scripts.services import analyze_sentiment
from fastapi import APIRouter, Depends
from Scripts.schemas import UserCreate, PostCreate, AnalysisResponse
from Scripts.models import User, Post


analysis_router = APIRouter()

@analysis_router.post("/register")
async def register_user(user: UserCreate):
    async with AsyncSessionLocal() as session:
        hashed_password = get_password_hash(user.password)
        new_user = User(username=user.username, password=hashed_password)
        session.add(new_user)
        await session.commit()
        return {"message": "User registered successfully."}


@analysis_router.post("/analyze", response_model=AnalysisResponse)
async def analyze_post(post: PostCreate, current_user: User = Depends(get_current_user)):
    async with AsyncSessionLocal() as session:
        sentiment = analyze_sentiment(post.content)
        keywords = extract_keywords(post.content)
        
        post_instance = Post(username=current_user.username, content=post.content)
        session.add(post_instance)
        await session.commit()
        
        return AnalysisResponse(sentiment=sentiment, keywords=keywords)