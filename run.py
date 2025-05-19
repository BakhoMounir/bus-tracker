# run.py

from app.services.azure_table import AzureTableService

azure_service = AzureTableService()

# Insert test location
azure_service.insert_or_update_bus_location("bus_test", 24.774265, 46.738586)

# Retrieve and print location
location = azure_service.get_bus_location("bus_test")
print(location)
