#App will ask city
#find city and use API to find 

import requests

count = 0

degree_sign = u"\N{DEGREE SIGN}" #Degree Sign

def celcToFar(num): #Converts Celsius to Fahrenheit

    far = (num * 9/5)+32
    return int(far)

wApi = "https://www.metaweather.com/api/location/search/" #MetaWeather API

area = input("Please Type in Closest Major City: ") #get Major city from user
location = requests.get(wApi + "?query="+ area)

# print(location.json()) #Prints Location.Json

jsonlocation = location.json()
woeid = jsonlocation[0]['woeid'] #Getting WoeID
City = jsonlocation[0]['title'] #Getting Full Name of City
print("City: "+ City)
print("Woeid: " + str(woeid))

lApi = "https://www.metaweather.com/api/location/" + str(woeid) #Location API

weather = requests.get(lApi)
jsonWeather = weather.json() #Gathering JSON Data

# day1 = jsonWeather.get('consolidated_weather')[0]
# day1Weather = day1.get('weather_state_name')
# day1Min = day1.get('min_temp')
# day1Max = day1.get('max_temp')
# day1Current = day1.get('the_temp')

# print("Todays Weather will feature: " + day1Weather)
# print("Todays Minimum Temperature will be: " + str(celcToFar(day1Min)) + degree_sign + "F")
# print("Todays Maximum Temperature will be: " + str(celcToFar(day1Max)) + degree_sign + "F")
# print("Todays Current Temperature is : " + str(celcToFar(day1Current)) + degree_sign + "F")

daysDisplayedEntered = input("How Many days would you like to see?: ") #Asks how many days from User
daysDisplayed = int(daysDisplayedEntered)
while int(daysDisplayed) > 6: #Max Days showed from MetaWeather is 6
    print("6 is Max, Please try again")
    daysDisplayedEntered = input("How Many days would you Like to see?: ")
    daysDisplayed = int(daysDisplayedEntered)
   



for f in jsonWeather.get('consolidated_weather'): #Grabbing Value from Keys
    
    day = jsonWeather.get('consolidated_weather')[count]
    dayWeather = day.get('weather_state_name')
    dayMin = day.get('min_temp')
    dayMax = day.get('max_temp')
    dayCurrent = day.get('the_temp')
    
    if count == daysDisplayed: break #Ends program when reaches days they asked for 

    if count ==0: #1st Day is Current Temperature
        print("Todays Weather will feature: " + dayWeather)
        print("Todays Minimum Temperature will be " + str(celcToFar(dayMin)) + degree_sign + "F")
        print("Todays Maximum Temperature will be " + str(celcToFar(dayMax)) + degree_sign + "F")
        print("Todays Current Temperature is " + str(celcToFar(dayCurrent)) + degree_sign + "F")
        print("---------------------------------") #Seperators between Texts
        count+=1
        continue
    else:
        print("Day " + str(count+1) + ": Weather will feature: " + dayWeather)
        print("Day " + str(count+1) +  ": Minimum Temperature will be " + str(celcToFar(dayMin)) + degree_sign + "F")
        print("Day " + str(count+1) +  ": Maximum Temperature will be " + str(celcToFar(dayMax)) + degree_sign + "F")
        print("Day " + str(count+1) +  ": Average Temperature will be " + str(celcToFar(dayCurrent)) + degree_sign + "F")
        print("---------------------------------")

        count+= 1