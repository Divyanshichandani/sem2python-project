from tkinter import *
from tkinter import ttk
import requests

API_KEY = "48e17a1d08e679066ba59ebbaf7bdd47"

def fetch_weather_data(city_name):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def data_get():
    city_name = city_entry.get()
    data = fetch_weather_data(city_name)

    if data is not None:
        weather_data = data['weather'][0]
        W_label1.config(text=weather_data["main"])
        Wb_label1.config(text=weather_data["description"])

        main_data = data['main']
        temp_label1.config(text=f"{int(main_data['temp'] - 273.15)}°C")
        per_label1.config(text=f"{main_data['pressure']} hPa")

win = Tk()
win.title("What's the forecast?")
win.config(bg="light blue")
win.geometry("600x600")

name_label = Label(win, text="WHAT'S THE FORECAST?", font=("courier new", 30, "bold"))
name_label.place(x=25, y=50, height=60, width=500)

city_entry = StringVar()
CITY_NAMES= ["Mumbai", "Delhi", "Kolkata", "Chennai", "Bangalore", "Hyderabad", "Ahmedabad", "Pune","Surat","Jaipur","Dehradun","Lucknow","Noida"]

city_combo = ttk.Combobox(win, text="Select a city", values=CITY_NAMES, font=("courier new", 30, "bold"), textvariable=city_entry)
city_combo.place(x=25, y=120, height=60, width=500)

done_button = Button(win, text="Done", font=["courier new", 20, "bold"], command=data_get)
done_button.place(y=190, height=50, width=100, x=200)

W_label = Label(win, text="Weather climate", font=("courier new", 15))
W_label.place(x=25, y=260, height=60, width=210)
W_label1 = Label(win, text="", font=("courier new", 10))
W_label1.place(x=250, y=260, height=60, width=210)

Wb_label = Label(win, text="Weather description", font=("courier new", 14))
Wb_label.place(x=25, y=330,height=60,width=210)
Wb_label1 = Label(win,text=(""), font = ("courier new", 10))
Wb_label1.place(x=250,y=330,height=60,width=210)

temp_label = Label(win,text=("temperature"), font = ("courier new", 15))
temp_label.place(x=25,y=400,height=60,width=210)
temp_label1 = Label(win,text=(""), font = ("courier new", 10))
temp_label1.place(x=250,y=400,height=60,width=210)


per_label = Label(win,text=("pressure"), font = ("courier new", 17))
per_label.place(x=25,y=470,height=60,width=210)
per_label1 = Label(win,text=(""), font = ("courier new", 10))
per_label1.place(x=250,y=470,height=60,width=210)

win.mainloop()