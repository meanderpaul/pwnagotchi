#!/bin/bash

# Update package list and install system dependencies
sudo apt-get update
sudo apt-get install -y python3-pip

# Install Python dependencies
pip3 install tensorflow scikit-learn pandas numpy google dbus-python file-read-backwards flask flask-cors flask-wtf gast gpiozero inky pycryptodome pydrive2 python-dateutil requests rpi-lgpio rpi_hardware_pwm scapy setuptools shimmy smbus smbus2 spidev toml tweepy websockets pisugar

# Execute any additional setup commands if needed

echo "Setup complete!"
