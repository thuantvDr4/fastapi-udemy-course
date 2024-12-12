from typing import Optional
from pydantic import BaseModel, Field


class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    description: str = Field(min_length=1, max_length=200)
    rating: int = Field(gt=0, le=5)
    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "title": "My Lady Love",
                "author": "Taylor Ann Bunker",
                "description": "When twenty year old, professional witch hunter, Victor Steep is summoned to handle a case",
                "rating": 4
            }
        }
    }
