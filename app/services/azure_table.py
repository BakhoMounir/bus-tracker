from azure.data.tables import TableServiceClient, TableEntity
from config import AZURE_CONNECTION_STRING, AZURE_TABLE_NAME
import datetime

class AzureTableService:
    def __init__(self):
        self.client = TableServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
        self.table_client = self._get_or_create_table(AZURE_TABLE_NAME)

    def _get_or_create_table(self, table_name):
        try:
            table = self.client.create_table_if_not_exists(table_name=table_name)
            print(f"[Azure] Table '{table_name}' ready.")
            return self.client.get_table_client(table_name=table_name)
        except Exception as e:
            print(f"[Azure Error] Could not create table: {e}")
            raise

    def insert_or_update_bus_location(self, bus_id, latitude, longitude):
        entity = {
            "PartitionKey": "BusLocation",
            "RowKey": str(bus_id),
            "Latitude": latitude,
            "Longitude": longitude,
            "Timestamp": datetime.datetime.utcnow().isoformat()
        }
        self.table_client.upsert_entity(entity)

    def get_bus_location(self, bus_id):
        try:
            entity = self.table_client.get_entity(partition_key="BusLocation", row_key=str(bus_id))
            return dict(entity)
        except Exception as e:
            print(f"[Azure Error] Could not retrieve entity: {e}")
            return None
