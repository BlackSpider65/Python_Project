
from tkinter import *
from tkinter import ttk
import requests

def data_get():
   city = city_name.get()
   data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=fc95afcf133968f2883b2b900f6f723d").json()
   weather_label1.config(text=data["weather"][0]["main"])
   dis_label1.config(text=data["weather"][0]["description"])
   tem_label1.config(text=str(int(data["main"]["temp"]-273.15)))
   pre_label1.config(text=data["main"]["pressure"])

root = Tk()
root.title("Wrather App")
root.config(bg="yellow")
root.geometry("520x520")

app_label = Label(root,text="Basic Wether App",font="comicsonsms 30 bold")
app_label.place(x=25,y=50,height=50,width=450)

city_name = StringVar()
states_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(root, text="Basic Wether App", values=states_name, font="comicsonsms 30 bold", textvariable=city_name)
com.place(x=35,y=120,height=40,width=430)

weather_label = Label(root,text="Weather Climate", font="comicsonsms 20 ")
weather_label.place(x=25,y=260,height=40,width=210)
weather_label1 = Label(root,text="", font="comicsonsms 20 ")
weather_label1.place(x=250,y=260,height=40,width=210)

dis_label = Label(root,text="Weather Discription", font="comicsonsms 20 ")
dis_label.place(x=25,y=330,height=40,width=245)
dis_label1 = Label(root,text="", font="comicsonsms 20 ")
dis_label1.place(x=280,y=330,height=40,width=230)

tem_label = Label(root,text="Temperature", font="comicsonsms 20 ")
tem_label.place(x=25,y=400,height=40,width=200)
tem_label1 = Label(root,text="", font="comicsonsms 20 ")
tem_label1.place(x=250,y=400,height=40,width=200)

pre_label = Label(root,text="Pressure", font="comicsonsms 20 ")
pre_label.place(x=25,y=470,height=40,width=200)
pre_label1 = Label(root,text="", font="comicsonsms 20 ")
pre_label1.place(x=250,y=470,height=40,width=200)


button = Button(root,text="Done", font="comicsonsms 30 bold", command=data_get)
button.place(x=150,y=190,height=40,width=200)

root.mainloop()