from sqlmodel import SQLModel, Field
from typing import List, Optional

class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    video: str
    likes: int
    comments: List[str] = []
    poster_id: int  # Foreign key to User
    climb_id: int  # Foreign key to Climb