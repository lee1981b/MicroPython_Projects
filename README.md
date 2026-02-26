# MicroPython_Projects

* A small collection of MicroPython projects, included also are a small collection of projects from the 
Freenove Ultimate Starter Kit. Updated as new Experiments & Projects come along. All Experiments & projects 
will be based on using Kali-Linux (Main OS) & Python (Version3.13), PyCharm IDE with the MicroPython-Tools Plugin 
package installed.

## Prerequisites:
- Kali-Linux/rolling Version 6.18.9
- Python Version 3.13
- esptool Version 5.2.0
- PyCharm Pro Version 2025.3.3
- MicroPython Tools (PyCharm Plugin) Pro Version 2026.1.3

## Project Structure:
Each project under ESP32_Projects is self-contained.  
Every folder contains only the files required to upload and run that specific build on the board.

## Project Uploading:
* Upload individual projects to the ESP32 boards. The following command will copy ony the files needed 
for that project.
```bash
mpremote cp boot.py :
mpremote cp main.py :
mpremote cp blink.py :
mpremote reset
```
## Getting Started:

1. blink_led, With this project you can see the LED is ON for one second and then OFF for one second, which
repeats in an endless loop.

2. button_led, With this project pushing the button switch turns the LED ON, Pushing the button again will turn the LED
OFF.

3.