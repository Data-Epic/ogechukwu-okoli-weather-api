import pytest # importing pytest library
# Adding the parent directory of the package
from api_interaction.weather_client import user_prompt

#checking for valid user prompt
def test_user_prompt_valid():
     user_prompt()
def test_user_prompt_invalid():
     user_prompt() # checking for invalid user prompt