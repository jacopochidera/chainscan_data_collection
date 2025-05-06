# Scripts/schemas.py

from pydantic import BaseModel
from typing import List

class UserCreate(BaseModel):
    username: str
    password: str

class PostCreate(BaseModel):
    content: str

class AnalysisResponse(BaseModel):
    sentiment: str
    keywords: List[str]
