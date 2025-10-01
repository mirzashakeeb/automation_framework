import pytest
from utils.api_client import create_booking, get_booking, update_booking, delete_booking
import allure

@allure.feature("Booking")
@allure.story("Create Booking")
def test_create_booking():
    data = {
        "firstname": "Mirza",
        "lastname": "Baig",
        "totalprice": 200,
        "depositpaid": True,
        "bookingdates": {"checkin": "2025-10-01", "checkout": "2025-10-05"},
        "additionalneeds": "Breakfast"
    }
    response = create_booking(data)
    booking = response.json()["booking"]
    assert booking["firstname"] == "Mirza"

# Similarly add GET, PUT, DELETE tests
