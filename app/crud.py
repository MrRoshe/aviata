import datetime

from sqlalchemy.orm import Session

from app.api import run
from app.models import Flight
from app.schemas import FlightCreate


def create_flight(db: Session, flight: FlightCreate, fly_from: str, fly_to: str):
    for item in run(fly_from=fly_from, fly_to=fly_to, date_from=datetime.date.today()):
        db_flight = Flight(
            fly_from=item["fly_from"],
            fly_to=item["fly_to"],
            date=item["date"],
            price=item["price"],
            booking_token=item["booking_token"],
            is_active=flight.is_active,
        )
        db.add(db_flight)
        db.commit()
        db.refresh(db_flight)

    return db_flight


def get_flights_by_from_to(db: Session, fly_from: str, fly_to: str):
    return (
        db.query(Flight)
        .filter(Flight.fly_from == fly_from and Flight.fly_to == fly_to)
        .all()
    )
