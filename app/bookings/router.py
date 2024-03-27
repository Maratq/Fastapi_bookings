from fastapi import APIRouter, Request, Depends
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.bookings.dao import BookingDAO
from datetime import date

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"],
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)):
    return await BookingDAO.find_all(user_id=user.id)


@router.post("")
async def add_booking(
        room_id: int,
        date_from: date,
        date_to: date,
        user: Users = Depends(get_current_user),
):
    await BookingDAO.add(user.id, room_id,
                         date_from, date_to)
