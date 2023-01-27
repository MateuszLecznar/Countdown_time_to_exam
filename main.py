import tkinter as tk
from tkinter import Label, StringVar
import sys
from datetime import datetime


def calculate_time():
    """
    Function countdown time to start exam Microprcessor technic at AGH
    :return: hours to end and minutes to end and second to end
    """
    format = '%Y-%m-%d %H:%M:%S'
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    real = datetime.strptime(str(dt), format)
    dm = datetime.strptime('2023-02-3 14:15:00', format)

    new = dm - real
    hours = int(new.total_seconds() / 3600)
    minutes = int(new.total_seconds() / 60 - hours * 60)
    seconds = int(new.total_seconds() - hours * 3600 - minutes * 60)
    return hours, minutes, seconds


def close(event):
    sys.exit()


def time_str():
    time = calculate_time()
    time_to_show = "  " + str(time[0]) + " godzin  " + str(time[1]) + " minut  " + str(time[2]) + " sekund   "
    return time_to_show


if __name__ == "__main__":
    start = True
    root = tk.Tk()
    root.title("Beginning of the end")

    var1 = StringVar()
    label = Label(root, textvariable=var1, font="Verdena 32 bold italic")
    label.pack()
    try:
        while (1):
            var1.set(time_str())
            root.update()
            root.bind('<Escape>', close)
    except:
        sys.exit()
