import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Schwab API credentials
SCHWAB_API_KEY = os.getenv('SCHWAB_API_KEY')
SCHWAB_API_SECRET = os.getenv('SCHWAB_API_SECRET')

# Add other configuration variables if needed
