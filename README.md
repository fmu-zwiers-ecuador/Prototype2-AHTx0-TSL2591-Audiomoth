# Prototype 2

This project logs environmental sensor data and records audio using a Raspberry Pi. All data is saved to a USB drive mounted at `/media/pi/BEAMdrive`.

## Files

- **Node_ID.txt**  
  Contains a unique ID for the device. Used to name the JSON data file.

- **read_ahtx0_tsl.py**  
  Reads data from the AHT20 (temperature, humidity) and TSL2591 (light) sensors. Appends readings to a JSON file on the USB drive.

- **record.py**  
  Records 5 minutes of audio from a connected microphone and saves it as a `.wav` file on the USB drive.

## Requirements

Install required libraries:

```bash
sudo pip install adafruit-circuitpython-ahtx0 --break-system-packages
sudo pip install adafruit-circuitpython-tsl2591 --break-system-packages
sudo pip3 install adafruit-blinka --break-system-packages
sudo pip install pyaudio --break-system-packages
sudo apt install portaudio19-dev python3-pyaudio
