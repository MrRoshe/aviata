import datetime

import sqlalchemy

from app.database import Base


class Flight(Base):
    __tablename__ = "flights"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    fly_from = sqlalchemy.Column(sqlalchemy.String, default="ALA")
    fly_to = sqlalchemy.Column(sqlalchemy.String, default="MOW")
    date = sqlalchemy.Column(sqlalchemy.DATE, default=datetime.date.today())
    price = sqlalchemy.Column(sqlalchemy.Integer, default=122)
    booking_token = sqlalchemy.Column(sqlalchemy.String, default="")
    is_active = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
