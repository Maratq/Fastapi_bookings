from app.dao.base import BaseDAO
from app.bookings.model import Bookings
from datetime import date
from sqlalchemy import select


class BookingDAO(BaseDAO):
    model = Bookings

    @classmethod
    async def add(cls,
                  room_id: int,
                  date_from: date,
                  date_to: date):
        booking_rooms = select(Bookings).where(
            and_(
                Bookings.room_id == 1,
                or_(
                    and_(
                        Bookings.date_from >= date_from,
                        Bookings.date_to <= date_to
                    ),
                    and_(
                        Bookings.date_from <= date_from,
                        Bookings.date_to > date_from
                    ),
                )
            )
        )

        rooms_left = (select(Rooms.quantity - func.count(booking_rooms.room_id))
                      .select_from(Rooms).join)