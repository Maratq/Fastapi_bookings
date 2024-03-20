from fastapi import FastAPI, Query, Depends
import uvicorn
from typing import Optional
from datetime import date
from pydantic import BaseModel
from app.bookings.router import router as router_bookings
from app.users.router import router as router_users

app = FastAPI()

app.include_router(router_bookings)
app.include_router(router_users)


class HotelSearchArgs:
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        has_spa: Optional[bool] = None,
        starts: Optional[int] = Query(None, ge=1, le=5),
    ) -> None:
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.starts = starts


@app.get("/hotels")
def get_hotels(search_args: HotelSearchArgs = Depends()):
    return search_args


class SBookin(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/bookings")
def add_booking(booking: SBookin):
    pass


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
