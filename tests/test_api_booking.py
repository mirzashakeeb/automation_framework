# tests/test_api_booking.py
import pytest
from utils.api_client import create_booking, get_booking


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

    # Ensure status code is 200
    assert response.status_code == 200

    # Access the nested booking dictionary
    booking_data = response.json()["booking"]

    # Assertions on the nested data
    assert booking_data["firstname"] == "Mirza"
    assert booking_data["lastname"] == "Baig"
    assert booking_data["totalprice"] == 200
    assert booking_data["depositpaid"] is True
    assert booking_data["bookingdates"]["checkin"] == "2025-10-01"
    assert booking_data["bookingdates"]["checkout"] == "2025-10-05"
    assert booking_data["additionalneeds"] == "Breakfast"
