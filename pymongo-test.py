import os
from pymongo import MongoClient

connection_string = os.environ.get('MONGODB_URL')

# Create a MongoClient
client = MongoClient(connection_string)

# Test the connection
try:
    # The ismaster command is cheap and does not require auth.
    client.admin.command('ismaster')
    print("Hello, World! Connection to MongoDB Atlas was successful.")
except Exception as e:
    print(f"Connection failed: {e}")
