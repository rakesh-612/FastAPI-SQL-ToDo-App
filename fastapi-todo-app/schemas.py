from pydantic import BaseModel;

# common class
class TodoBase(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id: int
    # To convert Python object to JSON response
    class Config:
        orm_mode = True