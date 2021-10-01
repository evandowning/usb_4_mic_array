# DOCS

## Requirements
  * Raspian
  * Python 3.7.3
  * pip
    * `$ sudo apt install python3-pip`
  * python3-pyaudio
    * `$ sudo apt install python3-pyaudio`

## Setup
  * `$ git clone --recursive git@github.com:evandowning/usb_4_mic_array.git`
  * `$ sudo pip3 install -r requirements.txt`

## Configure
  * `$ sudo python3 dfu.py --download 6_channels_firmware.bin`
  * `$ sudo python3 dfu.py --download 1_channel_firmware.bin`
  * Run `get_index.py` and enter index number into `record.py`

## Test microphone
  * `$ arecord -v -D plughw:2,0 -f cd -r 16000 test.wav`

## Usage
  * `$ python3 record.py --channel 1 --output test_1.wav`
