import tkinter as tk
import requests

HEIGHT = 400
WIDTH = 400


def get_weather(entry):
    print("This is the entry:", entry)


def format(weather):
    try:
        name = weather['name']
        info = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_string = 'City: {} \nConditions: {} \nTemperature: {}'.format(name, info, temp)
    except:
        final_string = 'Was not able to find information regarding {}'.format(name)

    return final_string


def get_weather(city):
    weather_key = '00437434884863c543bc074cd56ca6c3'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key,
              'q': city,
              'units': 'imperial'}

    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format(weather)


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='pic.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#e1d4ff', bd=5)
frame.place(relx=.5, rely=.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Wether", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#e1d4ff', bd=10)
lower_frame.place(relx=.5, rely=.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=40, anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()