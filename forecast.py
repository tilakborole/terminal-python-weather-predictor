import requests, json

def getForecastData(forecastdata):
	if forecastdata["cod"] == "404":
		print("Page not found. Enter correct spelling of the city")
		return
	forecast = forecastdata["list"]
	for x in  forecast:
		#For getting the data we are doing the same thing as we did in the last script
		#first we got date and time
		date = x["dt_txt"]
		y = x["main"]
		temperature = y["temp"]
		temperature_min = y["temp_min"]
		temperature_max = y["temp_max"]
		pressure = y["pressure"]
		humidity = y["humidity"]
		weather = x["weather"]
		description = weather[0]["description"]
		#Update temperatures to celcius
		temperature = temperature - 273.15
		temperature_min = temperature_min - 273.15
		temperature_max = temperature_max - 273.15
		#Now print all the details
		print("Date and Time : ", date)
		print("Predicted Temperature : ", temperature, " C")
		print("Maximum Temperature : ", temperature_max, " C")
		print("Minimum Temperature : ", temperature_min, " C")
		print("Pressure : ", pressure)
		print("Humidity : ", humidity)
		print("Weather : ", description)
		print("\n\n")
		

city_name = input("Enter city name : ")
api_key = "7dba78300ff303e43ad9f26ec564b7a5"
#We changed the base url slightly as we needed the forecast
base_url = "http://api.openweathermap.org/data/2.5/forecast?"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name 

response = requests.get(complete_url)
forecastdata = response.json()
getForecastData(forecastdata)

#For each day we will give data of 6AM, 12Noon, 6PM, 12Midnight Not Done that till now
