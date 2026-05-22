                                    ** MicroChip & Programmer Notes **

*MicroChip codes*
[24LC256-I/P] #Stores read only data.

### minipro, A CLI based Linux tool that enables the use of the T48 chip programer.
*Installation*
```zsh
sudo apt-get install build-essential pkg-config git libusb-1.0-0-dev zlib1g-dev
git clone https://gitlab.com/DavidGriffith/minipro.git
cd minipro
make
sudo make install
```
*Usage*
```zsh
sudo minipro -p T48
```
