from pydantic import BaseModel, Field


class NewNotedSchema(BaseModel):
    secret_fraze: str = Field(max_length=32)
    message: str = Field(max_length=512)