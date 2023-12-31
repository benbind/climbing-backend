from sqlmodel import SQLModel, Field
from typing import List, Optional, Tuple


class Location(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    latlon: Tuple[float, float]
    isIndoor: bool
    numberOfClimbs: int
    climbs: List[int] = []  # List of Climb IDs