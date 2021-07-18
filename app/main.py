from fastapi import Depends, FastAPI, status
from sqlalchemy.orm import Session

from app import crud
from app.models import Base
from app.schemas import FlightCreate
from app.database import SessionLocal, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/create_cash", status_code=status.HTTP_201_CREATED)
def create_cash(
    fly_from: str, fly_to: str, flight: FlightCreate, db: Session = Depends(get_db)
):
    crud.create_flight(db=db, flight=flight, fly_from=fly_from, fly_to=fly_to)


@app.get("/get_flights")
def show_flights(fly_from: str, fly_to: str, db: Session = Depends(get_db)):
    return crud.get_flights_by_from_to(db=db, fly_from=fly_from, fly_to=fly_to)
