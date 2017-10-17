# IOT LED Example for WEMOS ESP8266

This example is prepared for Introduction to Computers and Informatics class of TTU CyberSec Eng.

Details: https://wiki.itcollege.ee/index.php/Category:I600_Introduction_to_Computers_and_Informatics#Assignment:_Set_up_basic_IoT_scenario

## Requirements
* Python 3.x

## Running

First clone the repository to your computer via Git. Following commands are for Linux and Mac.
```sh
git clone https://github.com/yasinaydin/iot-led.git
cd iot-led
```

### On your machine

Run `main.py` like
```sh
python main.py
```
then browse to http://localhost:8080/

### On WEMOS

Run following command:

```sh
sudo ampy -p /dev/ttyUSB0 put main.py 
```

## Troubleshooting

### Resetting Device

If for any reason your device is struct, you may need to reset and reflash it.

Sample instructions do accomplish it are below for 32 and 64-bit.

32-bit:
```sh
wget http://micropython.org/resources/firmware/esp32-20171017-v1.9.2-279-g090b6b80.bin
sudo esptool.py -p /dev/ttyUSB0 -b 460800 erase_flash
sudo esptool.py -p /dev/ttyUSB0 -b 460800 write_flash --flash_mode dio 0x1000 esp32-*.bin
```

64-bit:
```sh
wget http://micropython.org/resources/firmware/esp8266-20170612-v1.9.1.bin
sudo esptool.py -p /dev/ttyUSB0 -b 460800 erase_flash
sudo esptool.py -p /dev/ttyUSB0 -b 460800 write_flash 0 esp8266-*.bin
```

### Using Different Baudrate

If the flashing (`ampy`) operation stalls or gives error, it might be because the file you are trying to send is too big and some parts of it may be lost during transmission. To try fixing it. you can try using different speeds. Baudrate parameter is used as `-b` in `ampy`. Default baudrate for AMPY is 115200.

Few examples are below. Note that the baudrates are multipliers of 1800.

```sh
sudo ampy -b 57600 -p /dev/ttyUSB0 put main.py 
sudo ampy -b 28800 -p /dev/ttyUSB0 put main.py 
sudo ampy -b 14400 -p /dev/ttyUSB0 put main.py 
```
