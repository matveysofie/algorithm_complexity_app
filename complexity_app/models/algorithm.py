from pydantic import BaseModel


class Algorithm(BaseModel):
    name: str
    description: str
    complexity: str
    code_example: str


