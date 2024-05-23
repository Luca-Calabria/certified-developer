from pydantic import BaseModel

class MaintenancePayload(BaseModel):
    temperature: int
    pressure: int

class SupportbotPayload(BaseModel):
    text_msg: str