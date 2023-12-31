from sqlmodel import SQLModel, Field
from typing import List, Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    photo: str
    highest_grade: int
    ascents: List[int] = []  # List of Post IDs
    location_id: int  # Foreign key to Location
