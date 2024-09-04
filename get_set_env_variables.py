import os

# Get environment variable
db_host = os.getenv('DB_HOST', 'localhost')

# Set environment variable
os.environ['DB_PORT'] = '5432'
