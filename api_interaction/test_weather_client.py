import pytest
from api_interaction.weather_client import user_prompt

# Adding the parent directory of the package
def test_user_prompt_valid():
     user_prompt()
def test_user_prompt_invalid():
     user_prompt()