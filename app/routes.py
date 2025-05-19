# app/routes.py

from flask import Blueprint, request, jsonify
from app.services.azure_table import AzureTableService

main_routes = Blueprint('main', __name__)
azure_service = AzureTableService()

@main_routes.route('/')
def home():
    return jsonify({"message": "Bus Tracker API is running."})

@main_routes.route('/update', methods=['POST'])
def update_location():
    data = request.get_json()
    bus_id = data.get('bus_id')
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    if not all([bus_id, latitude, longitude]):
        return jsonify({"error": "Missing required fields."}), 400

    azure_service.insert_or_update_bus_location(bus_id, latitude, longitude)
    return jsonify({"message": f"Location updated for bus {bus_id}."})

@main_routes.route('/location/<bus_id>', methods=['GET'])
def get_location(bus_id):
    location = azure_service.get_bus_location(bus_id)
    if location:
        return jsonify(location)
    return jsonify({"error": "Bus not found."}), 404
