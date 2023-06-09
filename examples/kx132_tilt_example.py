# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_kx132 import kx132

i2c = I2C(1, sda=Pin(2), scl=Pin(3))
kx = kx132.KX132(i2c)

kx.tilt_position_enable = kx132.TILT_ENABLED

while True:
    print(f"Current position {kx.tilt_position}")
    time.sleep(0.3)
