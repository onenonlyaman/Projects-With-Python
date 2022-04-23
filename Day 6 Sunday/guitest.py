import PySimpleGUI as sg

number = int(input('Specify your number: '))
layout = [[sg.Text('Welcome to times table maker!')],      
                 [sg.Text('Your Number'),sg.InputText(number)],
                 [sg.Submit(), sg.Cancel()]]      


window = sg.Window('Times Table Maker', layout)    

event, values = window.read()    
window.close()

text_input = values[0]    
sg.popup('You entered', text_input)

