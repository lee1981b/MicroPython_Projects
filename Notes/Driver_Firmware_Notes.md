                                ** Drivers & Firmware Notes **

### MicroPython Firmware.
- The micropython firmware for the ESP32 boards can be downloaded from the following site.
"https://micropython.org/download/ESP32_GENERIC/"

### Driver Packages.
*CH341PAR_LINUX*
- The CH341PAR_LINUX driver supports the following chipsets, CH341/CH346/CH347/CH339 USB to FIFO/SPI/I2C/GPIO. Supports CH346 480Mbps High-speed USB to Parallel FIFO/SPI, CH347 480Mbps High-speed USB to JTAG/SPI/I2C/GPIO, CH341 USB to SPI/I2C/EPP/MEM parallel port. The driver can be downloaded from the following GitHub Repo "https://github.com/WCHSoftGroup/ch341par_linux.git". See the README for installation instructions.
```zsh
make
sudo make install #Loads the driver on boot.
```

*CH341SER_LINUX*
- The ch341ser_linux driver supports the following chipsets, CH340 and CH341. The driver can be downloaded from the following GitHub Repo "https://github.com/WCHSoftGroup/ch341ser_linux". See the README for installation instructions.
```zsh
make
sudo make install #Loads the driver on boot.
```

### dfu-util, A CLI based tool for flashing firmware to Arduino boards. First place the Arduino board into it's bootloader mode, this can be achieved by either of the following methods.
*Method 1*
- On the main board Double Tap reset (Blue Button)
*Method 2*
- Open a python REPL, add tohe following code.
```python
import machine
machine.bootloader()
```
*Flash Firmware* 
- Download firmware from official site. "https://micropython.org/download/ARDUINO_GIGA/"
```zsh 
dfu-util -w -a 0 -d 2341:035b -D build-ARDUINO_GIGA/firmware.dfu
```

### Arduino-Giga micropython firmware installation.
*Download Repo*
```zsh
git clone https://github.com/micropython/micropython.git
cd micropython/ports/stm32
```
*Build for a specific board*
```zsh
make BOARD=ARDUINO_GIGA
```
*Put the board in DFU mode* 
```zsh
make BOARD=ARDUINO_GIGA deploy #Set BOOT0 to ON (connect BT0 to 3V3)
```
*Access the REPL via USB serial*
```zsh
screen /dev/ttyACM0 115200 #Set BOOT0 to OFF (connect BT0 to GND)
```

### esptool, A CLI based python tool for flashing the firmware over to the ESP32 boards. Ideally setup and install the esptool in a Virtual Environment. This saves any package clashes with Kalis apt package manager version if installed.
```zsh
uv venv .venv
source .venv/bin/activate 
uv pip install --upgrade esptool intelhex
esptool --chip esp32 --port /dev/ttyUSB0 erase-flash #Erase ESP32 flash.
esptool --chip esp32 --port /dev/ttyUSB0 --baud 460800 write-flash 0x1000 ESP32_GENERIC-20251209-v1.27.0.bin #Write firmware to ESP32
```
