# Burn Bryte Generator
## About The Project
This random generator started as I explored several new hobbies that I picked up during lockdown in 2020:

The Roll20 published RPG [Burn Bryte](https://marketplace.roll20.net/browse/bundle/5987/burn-bryte-starter-bundle) & Python programming.

This simple generator is intended primarily for GMs, as I found myself at a loss sometimes to quickly think of names for the unique species of Olaxis. Players that have difficulty coming up with name ideas can also find use for this tool.

## Installation and Usage
The name generator comes packaged as a zip file containing BBGen.exe and a supporting Data folder. If all you need is basic usage, simply unzip into a directory of your choice and run the executable.

Once it loads, simply click the button for each species to get a randomly generated name following their basic naming conventions or click on quit to close the generator.

### Linux install
If running on linux you may need to install the required packages `python3-tk` package for your OS and the associated `PySimpleGUI` for python3

for Ubuntu run this scriptpysimplegui
```bash
    sudo apt install python3-tk -y
    pip install PySimpleGUI
```

## Customizing the Lists
To support Homebrew and House Rules, the name lists can be added to and modified by finding the associated .txt files in the Data\SpeciesNames directory.

The README.txt file in that directory will explain the naming conventions used for each species to guide you if you choose to alter the lists contained in the subfolders.

## Contributing

See CONTRIBUTING.md for details.

## License
Licensed under the GNU General Public License v3.0

See LICENSE.txt for full details.
