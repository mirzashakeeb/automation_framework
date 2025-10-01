
# utils/api_client.py
import requests

BASE_URL = "https://restful-booker.herokuapp.com/booking"

def create_booking(data):
    response = requests.post(BASE_URL, json=data)
    return response

def get_booking(booking_id):
    return requests.get(f"{BASE_URL}/{booking_id}")

def update_booking(booking_id, data):
    return requests.put(f"{BASE_URL}/{booking_id}", json=data)

def delete_booking(booking_id):
    return requests.delete(f"{BASE_URL}/{booking_id}")
