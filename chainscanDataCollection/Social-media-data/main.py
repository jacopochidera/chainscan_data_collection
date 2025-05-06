# main.py

from fastapi import FastAPI
from contextlib import asynccontextmanager
from Scripts.routers import analysis_router  # import your routers
from fastapi.middleware.cors import CORSMiddleware
from Scripts.database import init_db

# Optional: setup DB or model loading here
# from Scripts.database import init_db, close_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()  # ← creates tables on app startup
    yield
app = FastAPI(lifespan=lifespan)

# Optional: Allow CORS for frontend dev/testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # use specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register your API routers
app.include_router(analysis_router, prefix="/api", tags=["Analysis"])

# Optional root route
@app.get("/")
async def root():
    return {"message": "Welcome to the Social Analysis API"}
