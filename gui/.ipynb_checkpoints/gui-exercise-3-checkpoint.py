# Exercise 3: To-Do List

import PySimpleGUI as sg

tasks = []

layout = [[sg.InputText(), sg.Button("Add")],
          [sg.Listbox(values=tasks, size=(40, 10), key="-LIST-")],
          [sg.Button("Delete"), sg.Button("Mark as Completed"), sg.Button("Exit")]]

window = sg.Window("To-Do List", layout, size=(350, 350))

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    if event == "Add" and values[0] != "":
        tasks.append(values[0])
        window["-LIST-"].update(values=tasks)
        window[0].update("")
    if event == "Delete" and len(values["-LIST-"]) > 0:
        tasks.remove(values["-LIST-"][0])
        window["-LIST-"].update(values=tasks)
    if event == "Mark as Completed" and len(values["-LIST-"]) > 0:
        tasks.remove(values["-LIST-"][0])
        window["-LIST-"].update(values=tasks)

window.close()
