import PySimpleGUI4 as sg
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from train2 import make_image


def select_files():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    return filename

# select_files() # <- nie dziala rn na linuxie

def browse_images():

    layout = [
        [sg.Image(key='img', filename='logo.png')],
        [sg.Button("browse", key='browse')],
    ]

    window = sg.Window(title="Results", layout=layout, margins=(100, 50))

    def update_image():
        window['img'].update(filename='temp.png', visible=True)
        window.refresh()

    while True:
        event, values = window.read()
        print(event)

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == 'browse':
            filename = select_files()
            make_image(filename)
            update_image()
        #text_input = values[0]
        #sg.popup('You entered', text_input)

browse_images()
