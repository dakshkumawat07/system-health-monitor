import platform
import os
import psutil


print("========================================")
print("       SYSTEM HEALTH MONITOR")
print("========================================")
print()

print("Operating System :", platform.system())
print("System           :", platform.release())
print("Machine          :", platform.machine())
print("Logical CPUs     :", os.cpu_count())
print("Processor        :", platform.processor())

memory = psutil.virtual_memory()


print("Memory Total     :", round(memory.total / (1024 ** 3), 2), "GB")
print("Memory Available :", round(memory.available / (1024 ** 3), 2), "GB")
print("Memory Used      :", round(memory.used / (1024 ** 3), 2), "GB")
print("Memory Usage     :", memory.percent, "%")
print("Python Version   :", platform.python_version())

print()
print("========================================")
