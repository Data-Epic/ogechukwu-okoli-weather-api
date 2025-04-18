# ogechukwu-okoli-weather-api
# Weather API Project

Welcome to the Weather API project, a Python-based application for fetching and displaying weather data for multiple cities using OpenWeather API.
This python script retrives weathe data across several cities for 5 days in a 3 hour interval
This project demonstrates how to interact with a weather API and includes automated tests to verify functionality.

## Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Testing](#testing)

## Project Overview

This project allows users to:
- Input a list of city names and fetch corresponding weather information via an API.
- View formatted weather data for each specified city.
- Decide whether to continue with additional requests or exit the application after each batch of API calls.

The application leverages Python's Requests library for making HTTP requests, and it is structured in a modular way to facilitate maintenance and scalability.

## Project Structure

The project is organized as follows:
api_interaction_okoli_ogechukwu_abimbola|api_interaction # Contains the main source code for the API interaction logic.│test_weather_client.py # Contains automated tests for the project..py  │weather_client_prompt # Contains the use functions and API-calling logic
## Installations needed for this script
pip install requests,,pytest,dotenv,os,regex

## Testing
Testing was done in the tests folder using pytest.
# Running Tests with Pytest

This document explains how to run your tests using `pytest` with the `-v` (verbose) and `-s` (disable output capturing) flags.

## Overview

- **`-v` (Verbose):**
  The `-v` flag increases the verbosity level of the output so that pytest prints additional details about which tests are being run and their statuses.

- **`-s` (Disable Output Capturing):**
  The `-s` flag disables the capturing of standard output and standard error. This is useful when you need to see all printed output in real-time (for example, for debugging tests that involve `input()` calls or logging).

## Steps to Run Tests

1. **Open a Terminal or Command Prompt:**

   Navigate to the root directory of your project where your test files are located.

2. **Run the Tests:**

   Execute the following command:

   ```bash
   pytest -v -s