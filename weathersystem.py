import requests
import json
import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")
city=input("Enter the name of the city to check the temprature :")
url=f"https://api.weatherapi.com/v1/current.json?key=81f8181878d2464f893170150231906&q={city}"
r=requests.get(url)
                                   #print(r.text) prints the complete json file with all details but we just need the temprature.
temp_obj=json.loads(r.text)        #Here's how json.load() is typically used:

#Open a file: First, you need to open a file containing JSON data using the open() function. It returns a file object.

#Read JSON data: Pass the file object to json.load() as an argument. This function reads the contents of the file and parses the JSON data, converting it into a corresponding Python object.

#Access the data: The returned Python object can be accessed and manipulated like any other Python object. It can be a dictionary, list, string, number, boolean, or a combination of these data types, depending on the JSON structure.


try:
    print(f"Temprature:{temp_obj['current']['temp_c']}")
    print(f"Region:{temp_obj['location']['region']}")
    print(f"Country:{temp_obj['location']['country']}")
    print(f"last update:{temp_obj['current']['last_updated']}")
    text = f"Temprature:{temp_obj['current']['temp_c']}"
    speak.Speak(text)
    text1 =f"Region:{temp_obj['location']['region']}"
    speak.Speak(text1)
    text2=f"Country:{temp_obj['location']['country']}"
    speak.Speak(text2)
    text3=f"last update:{temp_obj['current']['last_updated']}"
    speak.Speak(text3)


except requests.exceptions.HTTPError as err:
    print(f"Error:{err}")
    speak.Speak("An error occured while retriving the weather informatino you asked!")

except json.JSONDecodeError:
    print("Error: Invalid response from the weather API.")
    speak.Speak("An error occurred while parsing the weather information.")

except Exception as e:
    print(f"Error: {e}")
    speak.Speak("An unexpected error occurred.")