# hello_world.py

import PySimpleGUI4 as sg

image_paths = [f'/home/omahayomaso/Projects/FUN/zespol-wiosna-ai/images_for_ui/KOTEL1_walk{x}.png' for x in range(1,3)]

print(image_paths)
layout = [
    [sg.Image(key='img', filename=image_paths[0])],
    [sg.Button("next", key='next'), sg.Button("prev", key='prev')],
]

window = sg.Window(title="Hello World", layout=layout, margins=(100, 50))

idx = 0


def update_image(idx):
    window['img'].update(filename=image_paths[idx], visible=True)
    window.refresh()


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
