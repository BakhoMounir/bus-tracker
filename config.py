# config.py
import os
from dotenv import load_dotenv

load_dotenv()

AZURE_TABLE_NAME = os.getenv("AZURE_TABLE_NAME")
AZURE_CONNECTION_STRING = os.getenv("AZURE_CONNECTION_STRING")
