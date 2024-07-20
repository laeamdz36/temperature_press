"""Checking temperature on the MAIN CPU"""

from gpiozero import LEDBarGraph, CPUTemperature
from signal import pause

cpu = CPUTemperature()
print(f"Current temperature: {cpu.temperature}")
