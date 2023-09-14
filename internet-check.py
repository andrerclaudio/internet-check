"""
It is initialized as a service.
"""

import os
import time
import requests

# Define the number of retries and other configuration options
MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 60
CHECK_URL = "https://www.google.com"

def internet_check():

    attempts = 0

    while True:

        try:
            # Attempt to send a GET request to the configured URL
            response = requests.get(CHECK_URL, timeout=5)
            # If the response status code is 200, it means the request was successful
            if response.status_code == 200:
                attempts = 0  # Reset the attempts counter upon success
            else:
                # Anything differente means the device is not connected or something is wrong
                attempts += 1

        except requests.ConnectionError:
            # If an exception is raised, it means the device is not connected to the internet
            attempts += 1

        # If we've reached the maximum number of retries without success, reboot the system
        if attempts >= MAX_RETRIES:

            # Attempt to reboot the system and handle any exceptions
            try:
                os.system("sudo reboot")
                # Exit the loop since the system will restart
                break

            except Exception as e:
                pass

        # Sleep for a custom delay before the next attempt
        time.sleep(RETRY_DELAY_SECONDS)


if __name__ == "__main__":
    # Check for internet connection and force Reset when there is none.
    internet_check()
