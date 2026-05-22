                                        ** General Notes **

### The official list of MicroPython-supported Arduino boards includes to following devices.
*Nano 33 BLE*
*Nano 33 BLE Sense*
*Nano RP2040 Connect*
*GIGA R1 WiFi*
*Portenta H7*

### IOT Analysis & Debugging Tools, Connect devices via USB or RXTX-to-USB.
```zsh
pulseview 
sigrok-cli 
```

### ESP32 Pins and GPIO Numbers.

*Input or Output functions*
Pins: [0-19, 21-23, 25-27, 32-39]

*REPL UART TXRX*
Pins: [1, 3]

*Embedded Flash PINS*
Pins: [6, 7, 8, 11, 16, 17]

*Input Only*
Pins: [34, 35, 36, 37, 38, 39]

### Use the following header when creating micropython scripts.
```python 
#!/opt/bin/lv_micropython
```

### micropython-stubs is a collection of various modules created for micropython scripting projects. These can be installed to any project then used as required, Ideally setup a VENV then install the correct package via pip. 
```zsh
uv venv .venv
source .venv/bin/activate
uv pip install "micropython-esp32-stubs==1.26.0.*"
```

