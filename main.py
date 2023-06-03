from typing import Optional, List
from fastapi import FastAPI, Path, Query
from api import courses, sections, users

app = FastAPI(
    title="FastAPI RB",
    description="Building app for managing students and courses.!",
    version="0.0.1",
    contact={
        "name": "Rajesh Baghel",
        "email": "rajeshb3297@gmail.com",
    },
    license_info={
        "name": "MIT",
    }
)

app.include_router(courses.router)
app.include_router(sections.router)
app.include_router(users.router)



