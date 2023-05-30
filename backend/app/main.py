from fastapi import FastAPI
import models
from database import engine
from routers import user, auth, recommendations
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


models.Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(recommendations.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
