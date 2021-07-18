import datetime

from pydantic import BaseModel


class FlightBase(BaseModel):
    fly_from: str
    fly_to: str
    date: datetime.date
    price: int
    booking_token: str
    is_active: bool


class FlightPrint(BaseModel):
    fly_from: str
    fly_to: str
    date: datetime.date
    price: int
    is_active: bool

    class Config:
        orm_mode = True


class FlightCreate(FlightBase):
    pass


class Flight(FlightBase):
    id: int

    class Config:
        orm_mode = True
