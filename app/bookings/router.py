from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"],
)


@router.get("/bookings")
def get_bookings(request: Request):
    return dir(request)


@router.get("/{booking_id}")
def get_bookings2(booking_id):
    pass
