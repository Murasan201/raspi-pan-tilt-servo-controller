# raspi-pan-tilt-servo-controller

Python application for controlling SG90 pan-tilt servos with the Adafruit 16-Channel PWM/Servo HAT on Raspberry Pi 5.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)
- [Author](#author)

## Prerequisites

- Raspberry Pi 5 running Raspberry Pi OS
- Adafruit 16-Channel PWM/Servo HAT
- SG90 servo motors
- I2C interface enabled on the Raspberry Pi
- Python 3.x
- [CircuitPython ServoKit library](https://github.com/adafruit/Adafruit_CircuitPython_ServoKit)

## Installation

1. Update package lists:
   ```bash
   sudo apt update
   ```
2. Install system dependencies:
   ```bash
   sudo apt install -y python3-pip python3-venv i2c-tools
   ```
3. Enable I2C interface if not already enabled:
   ```bash
   sudo raspi-config
   # Navigate to Interface Options -> I2C -> Enable
   ```
4. Create and activate a Python virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
5. Install required Python libraries:
   ```bash
   pip install adafruit-blinka adafruit-circuitpython-servokit
   ```

Alternatively, to install system-wide (if not using a virtual environment):
   ```bash
   sudo python3 -m pip install adafruit-blinka adafruit-circuitpython-servokit --break-system-packages
   ```

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/USERNAME/raspi-pan-tilt-servo-controller.git
   cd raspi-pan-tilt-servo-controller
   ```
2. Run the application:
   ```bash
   python3 pan_tilt_demo.py
   ```
3. Use Ctrl+C to stop; servos will reset to neutral (90°).

## Configuration

- Adjust pulse width range in `pan_tilt_demo.py` if your servos require different calibration.
- Change servo channels if you connect to channels other than 0 (pan) and 1 (tilt).
- Modify sweep speed by changing `time.sleep()` intervals.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

**Murasan**  
Website: https://murasan-net.com/
