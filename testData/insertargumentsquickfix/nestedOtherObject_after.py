from typing import Optional
from pydantic import BaseModel, Field


class A(BaseModel):
    a: int
    b: int = ...
    c: int = 123
    d: int = Field(123)
    e: int = Field(...)
    f: Optional[int]


str(A(a=int(), c=2, b=, d=123, e=, f=))
