from fastapi import FastAPI
from domain.langchain import langchain_router
from domain.githubqa import gitqa_router

app = FastAPI()

app.include_router(gitqa_router.router)
app.include_router(langchain_router.router)