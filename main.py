# Librires to get request and response and pars json and print it with pprint
import requests, json, pprint

# Website use for get the information https://www.openweathermap.org
# API_key
API_key = 'put your API here'

while True:
    # Ask user for city name or quit
    userInput = input("Give the name of the city or (Q) for quit: ")

    if userInput != 'Q':
        # Get the city latitude and longitude
        geocodingAPI = f'http://api.openweathermap.org/geo/1.0/direct?q={userInput}&appid={API_key}'

        # Get back the response
        response = requests.get(geocodingAPI)

        # Check if we get data
        if response.status_code == 200:
            # pars data to json
            data = json.loads(response.text)

            # Get the lat and lot from the response
            lat = data[0]['lat']
            lon = data[0]['lon']

            # Call the weatherAPI with Lat and Long 
            weatherAPI = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
            
            # Get the weather response from the API
            weatherResponse = requests.get(weatherAPI)

            # check if we get data
            if weatherResponse.status_code == 200:
                # Pars data to json
                data = json.loads(weatherResponse.text)

                # Get the information we need
                humidity = data['main']['humidity']
                temp = data['main']['temp']
                weather = data['weather'][0]['main']
                
                # Print it to the user
                print(f'Weather: {weather}, Temperature: {temp}, Humidity: {humidity}')
                continue
            else:
                print(f"Error: {weatherResponse.status_code}")
        else:
            print(f"Error: {response.status_code}")
    else:
        print("Thanks for using our APIs")
        break