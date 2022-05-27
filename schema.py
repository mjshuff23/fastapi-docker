from typing import Union

from pydantic import BaseModel


class User(BaseModel):
    first_name: str
    last_name: Union[None, str] = None
    age: int

    class Config:
        orm_mode = True
