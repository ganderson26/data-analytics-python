# Exercise 2: Simple Calculator

import PySimpleGUI as sg

layout = [[sg.InputText(size=(15, 1), key="-INPUT-"), sg.Text("0", size=(15, 1), key="-OUTPUT-")],
          [sg.Button("+"), sg.Button("-"), sg.Button("*"), sg.Button("/")],
          [sg.Button("Clear"), sg.Button("Exit")]]

window = sg.Window("Simple Calculator", layout, size=(350, 150))

print("Output")

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    if event == "Clear":
        window["-INPUT-"].update("")
        window["-OUTPUT-"].update("")
    else:
        try:
            result = eval(values["-INPUT-"])
            print(result)

            if event == "+":
                answer = float(window["-OUTPUT-"].get()) + result
            if event == "-":
                answer = float(window["-OUTPUT-"].get()) - result
            if event == "*":
                answer = float(window["-OUTPUT-"].get()) * result
            if event == "/":
                answer = float(window["-OUTPUT-"].get()) / result            

            print(answer)
            window["-OUTPUT-"].update(answer)
        except:
            window["-OUTPUT-"].update("Error")

window.close()
