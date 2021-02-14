#!/usr/bin/env python3

import PySimpleGUI as sg

from lib.name_list import NameGen

name = NameGen()

# Define the window's contents
layout = [
    [sg.Text("What species is your character?")],
    [sg.Text(size=(40, 2), key="-OUTPUT-")],
    [
        sg.Button("Driftling"),
        sg.Button("Glean"),
        sg.Button("Ino"),
        sg.Button("Kith'uk"),
        sg.Button("Peacecraft"),
        sg.Button("Ror-nan"),
        sg.Button("Ulran"),
        sg.Button("Zivoy"),
    ],
    [sg.HorizontalSeparator()],
    [sg.Button("Quit", pad=(4, 6))],
]

# Create the window
window = sg.Window("Chris's Burn Bryte Name Generator v1.0", layout, background_color="")

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == "Quit":
        break
    elif event == "Driftling":
        window["-OUTPUT-"].update(name.driftling_name())
    elif event == "Glean":
        window["-OUTPUT-"].update(name.glean_name())
    elif event == "Ino":
        window["-OUTPUT-"].update(name.ino_name())
    elif event == "Kith'uk":
        window["-OUTPUT-"].update(name.kithuk_name())
    elif event == "Peacecraft":
        window["-OUTPUT-"].update(name.peacecraft_name())
    elif event == "Ror-nan":
        window["-OUTPUT-"].update(name.rornan_name())
    elif event == "Ulran":
        window["-OUTPUT-"].update(name.ulran_name())
    elif event == "Zivoy":
        window["-OUTPUT-"].update(name.zivoy_name())


# Finish up by removing from the screen
window.close()
