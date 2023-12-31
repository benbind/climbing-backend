from sqlmodel import SQLModel, Field
from typing import List, Optional

class Climb(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    grade: int
    location_id: int  # Foreign key to Location
    rating: int
    name: str
    ascents: List[int] = []  # List of Post IDs