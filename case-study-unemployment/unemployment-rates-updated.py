# Update the GUI to allow the User to enter a range of Years

import PySimpleGUI as sg
import matplotlib.pyplot as plt
import pandas as pd 

# Create function reate the plot
def create_plot(year, unemployment_rate):
    plt.plot(year, unemployment_rate, color='red', marker='o')
    plt.title('Unemployment Rate By Year', fontsize=14)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Rate', fontsize=14)
    plt.grid(True)
    return

# Define the layout
layout = [[sg.Text("Starting Year"), sg.InputText("1948", size=(10, 1), key="start_year"),
          sg.Text("Ending Year"), sg.InputText("2024", size=(10, 1), key="end_year")],
          [sg.Button('Show')]]

# Create the window
window = sg.Window('Unemployment Rates for Selected Years', layout, size=(350, 150))

# Create DataFrame from reading Excel file using pandas
# pandas is using openpyxl depending on the file extension under the hood
df = pd.read_excel('updated-unemployment.xlsx', sheet_name='Sheet1', usecols='B:N')

# A little debugging
#print(df.head())
#print(df['Year'])

# Event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Show':
        # Get the Year range
        start = int(window["start_year"].get())
        end = int(window["end_year"].get())
        # https://www.geeksforgeeks.org/how-to-fix-valueerror-the-truth-value-of-a-series-is-ambiguous-in-pandas/
        range_df = df[(df['Year'] >= start) & (df['Year'] <= end)]

        print(range_df)
        
        # Get the average of the months for the years selected
        # To compute row averages, set the axis parameter to 1
        range_df['Avg'] = range_df[['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']].mean(axis=1)

        print(range_df)
       
        create_plot(range_df['Year'], range_df['Avg'])
        
        plt.show(block=False)

# Close window
window.close()