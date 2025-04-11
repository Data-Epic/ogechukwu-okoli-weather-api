import pytest # importing pytest library
# Adding the parent directory of the package
from api_interaction.weather_client import user_prompt

def test_user_prompt_valid():#checking for valid user prompt
     user_prompt()
def test_user_prompt_invalid():# checking for invalid user prompt
     user_prompt()