from pydantic import BaseModel, Field


class NewNotedSchema(BaseModel):
    password: str = Field(max_length=32)
    message: str = Field(max_length=512)