import PySimpleGUI4 as sg
from tkinter import Tk
from tkinter.filedialog import askopenfilename

image_paths = [f'/home/omahayomaso/Projects/FUN/zespol-wiosna-ai/images_for_ui/KOTEL1_walk{x}.png' for x in range(1,3)]

print(image_paths)

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

def select_files():
    layout = [
        [sg.FolderBrowse(key='img')],
    ]

    window = sg.Window(title="Select files", layout=layout, margins=(100, 50))

    while True:
        window.read()

# select_files() # <- nie dziala rn na linuxie

def browse_images(image_paths):

    layout = [
        [sg.Image(key='img', filename=image_paths[0])],
        [sg.Button("prev", key='prev'), sg.Button("next", key='next')],
    ]

    window = sg.Window(title="Results", layout=layout, margins=(100, 50))

    def update_image(idx):
        window['img'].update(filename=image_paths[idx], visible=True)
        window.refresh()

    idx = 0

    while True:
        event, values = window.read()
        print(event)

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == 'next':
            idx += 1
            update_image(idx)

        if event == 'prev':
            idx -= 1
            update_image(idx)

        #text_input = values[0]
        #sg.popup('You entered', text_input)

browse_images(image_paths)
