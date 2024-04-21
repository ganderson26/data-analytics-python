# Exercise 1: Personalized Greeting

import PySimpleGUI as sg

# Define the layout
layout = [[sg.Text("Enter your name:"), 
           sg.InputText()],
          [sg.Button("Submit")]]

# Create the window
window = sg.Window("Greeting App", layout, size=(350, 150))

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    # Window popup
    # There is no size parameter for the sg.popup(). Use spaces and empty strings like paddings
    sg.popup(f"       Hello, {values[0]}!         ")

# Close the window
window.close()
