import pytest # importing pytest library
import sys
import os

# Adding the parent directory of the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Adding the parent directory of the package
from api_interaction.weather_client import user_prompt

def test_user_prompt_valid():#checking for valid user prompt
     user_prompt()
def test_user_prompt_invalid():# checking for invalid user prompt
     user_prompt()