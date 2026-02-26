* How to download & set up the MicroPython firmware for the ESP32 boards using the Linux CLI. 
Plus how to install the correct tools required for flashing the firmware.

* I personally like to use the esptool provided by the Python pip package manager for flashing the MicroPython
firmware onto the ESP32 boards. Also note this package is not to be confused with the apt package manager version,
the apt package will throw errors about missing packages. To install the correct version you can use the 
following command: 
``` bash
python3 -m pip install --user --upgrade esptool
``` 

* Setup USB permissions by adding by adding user to the dialout group. This will help any Serial permission errors.
Log out & back in for the command to take effect.
```bash
sudo usermod -aG dialout $USER
```

* You may also require the ch341ser_linux driver if the ESP32 boards are not recognized by Kali.
The Driver package can be found on github at the following address "https://github.com/WCHSoftGroup/ch341ser_linux".
The same driver package is also available in this repository. Once downloaded the package can be installed
and made to load on boot using the following commands:
```bash
cd ch341ser_linux
make
sudo make install
```

* Once installed we can check the ESP32 board is being recognized using any or all of the following CLI tools:
```bash
lsusb 
lsblk
usb-devices
inxi -D -x
ls /dev/ttyUSB*
```

* Download the current MicroPython firmware, The following website provides all versions of the firmware 
"https://micropython.org/download/ESP32_GENERIC/". Download the latest .bin version for the correct board.

* Flash the MicroPython firmware to the ESP32 board. Connect the board via USB (Make sure you are using a data cable).
Erase any pre-installed programs on the board first then flash the firmware using the esptool. 
Use the following commands to erase & flash the firmware.
```bash
python3 -m esptool --chip esp32 --port /dev/ttyUSB0 erase_flash
python3 -m esptool --chip esp32 --port /dev/ttyUSB0 --baud 460800 write-flash 0x1000 ESP32_GENERIC-20251209-v1.27.0.bin
```

* The flash will take a minute or two to write to the board. Once flashed, MicroPython will be functional
on the ESP32 and ready to accept and run Python scripts.

* Verify the flash uploaded all ok by checking for a quick Python REPL on the ESP32 board. Use either of the 
following CLI tools to check the ESP32 board.
```bash
screen /dev/ttyUSB0 115200
picocom /dev/ttyUSB0 -b 115200
```
* Then confirm by Pressing the reset button on the ESP32 board, you should then see the MicroPython REPL prompt: >>>
