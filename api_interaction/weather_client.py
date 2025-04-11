import requests # importing requests library
import regex as re # impporting regex for matching strings
from dotenv import load_dotenv # importing library for hiding api key
import os # importing os library

load_dotenv() # loading .env file as environmental variables

# Function to call the API and return the data for one city
def call_api(city_name, api_key):
    """
    Function to read the contents of the API that takes in two arguments city_name nad api_key to dynamically load the weather details of several cities
    Error handling is duly accounted for in this function using try except block.

    The try error block takes in the url, gets the status(200) is API call was successful.
    Then uses the request library base call for trigerring exception in cases of 4**,5** errors
    The first except block checks for HTTP error that is error with status code
    the second checks requests.exceptions.RequestException) is a base exception class in the Requests library that serves as the parent for all exceptions raised by
    the third exception block checks for any other possible error that may occur outside of the requests library
    """
    try:
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units=metric" # url for api
        response = requests.get(url)
        response.raise_for_status() # base calls for checking errors in the request library
        return response.json() # reading the json output from the API

    except requests.exceptions.HTTPError as http_err: # http errors with status code
        print(f"HTTP error for {city_name}: {http_err}")
    except requests.exceptions.RequestException as req_err: # handling anyother error caused by the base class for exceptions in hte requests library
        print(f"Request error for {city_name}: {req_err}")
    except Exception as err: # code to catch any other unexpected errors
        print(f"An error occurred for {city_name}: {err}")

# Function to get weather data by looping through the Json response
def get_data(data):
    """"
    Looping throught the json response to get the contenst i desire.
    The name of the city is not contained in the list parameter, it is located in the initial Json response before the nested list.
    """
    if "list" in data and "city" in data:
        name = data["city"]["name"] # varaiable for accessing the city name from the json response
        print(f"\nWeather forecast for {name} for the next five days with 3 hour interval:\n") #printing the city name using string formatting
        # for loop for loopin through the nested loop in the json response to get the required weather data i need
        for item in data['list']:
            dt_txt = item['dt_txt'] # date
            temp = item['main']['temp'] # temperature
            weather = item['weather'][0]['description']# weather description
            speed = item["wind"]["speed"]# wind speed
            humidity = item["main"]["humidity"]# level of humidity
            print(f"Date:{dt_txt},Temp:{temp}°C,Weather:{weather},Wind:{speed} m/s,Humidity:{humidity}%")# Output for weather data using string formatting
    else:
        print("No forecast data found in the API") # output if the above parameters are not available

# function demanding user prompt named user_prompt.
def user_prompt():
    api_key = os.getenv("WEATHER_API_KEY")# variable for loading api key using os.getenv as an environmetal variable to kee

    while True:
        cities = input("\nEnter city names separated by commas (e.g.Abuja,Lagos): ")

        if cities:
            city_list = [city.strip() for city in re.split(r',+', cities) if city.strip()]
            print(f"\nCity list: {city_list}")

            confirm = input("Fetch weather for these cities? (y/n): ").strip().lower()
            if confirm == "y".lower():
                for city in city_list:
                    print(f"\nFetching weather for: {city}")
                    data = call_api(city, api_key)
                    if data:
                        get_data(data)
                        """
                        Continuously prompt the user for a decision to continue fetching weather information.
                        This inner loop persists until the user enters a valid choice:
                        - If 'y' is entered, the loop breaks, returning control to the outer loop to fetch weather for new cities.
                        - If 'n' is entered, the loop terminates the function after printing a termination message using retun since it is a nested while loop
                        - Any other input prompts an error message and the loop repeats.
                        """
                while True:  # Ask until user gives a valid choice
                    choice = input("Do you want to continue? (y/n): ").strip().lower()
                    if choice == "y".lower():
                        break  # go back to top of outer while loop
                    elif choice == "n".lower():
                        print("The end!")
                        return  # exit the function
                    else:
                        print("Invalid input. Please type 'y' or 'n'.")
                """
                A part of the inital while loop to prompt the user if the do not want to continue with the current list of cities inputted by parsing 'n' and the loop breaks after printing Existing
                In cases where the user provides an invalid input, the while loop prints "Invalid input"  and prompts the user to input a city/cities name
                Under circumstances where the inout statement is left blank, "Please enter at least one city" is printed and the user is prompted to input a city name
                """
            elif confirm == "n".lower():
                print("Exiting.")
                break
            else:
                print("Invalid input")
        else:
            print("Please enter at least one city.")
user_prompt()#calling the user_prompt function