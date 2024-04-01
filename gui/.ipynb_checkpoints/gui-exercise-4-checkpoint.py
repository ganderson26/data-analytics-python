import PySimpleGUI as sg
import matplotlib.pyplot as plt
import pandas as pd 

# Create function reate the plot
def create_plot(year, unemployment_rate):
    plt.plot(year, unemployment_rate, color='red', marker='o')
    plt.title('Unemployment Rate Vs Year', fontsize=14)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Rate', fontsize=14)
    plt.grid(True)
    return

# Define the layout
layout = [[sg.Button('Show')]]

# Create the window
window = sg.Window('Embedding Matplotlib In PySimpleGUI', layout, size=(350, 50))

# Create DataFrame from reading Excel file using pandas
# pandas is using openpyxl depending on the file extension under the hood
df = pd.read_excel('unemployment.xlsx', sheet_name='Sheet', usecols='A:B')

# A little debugging
print(df.head())
print(df['Year'])

# Event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Show':
        create_plot(df['Year'], df['Rate'])
        plt.show(block=False)

# Close window
window.close()