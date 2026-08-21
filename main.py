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
print("Processor        :", platform.processor())
print("Logical CPUs     :", os.cpu_count())

cpu_usage = psutil.cpu_percent(interval=1)

print("CPU Usage        :", cpu_usage, "%")
memory = psutil.virtual_memory()


print("Memory Total     :", round(memory.total / (1024 ** 3), 2), "GB")
print("Memory Available :", round(memory.available / (1024 ** 3), 2), "GB")
print("Memory Used      :", round(memory.used / (1024 ** 3), 2), "GB")
print("Memory Usage     :", memory.percent, "%")

disk = psutil.disk_usage("/")

print("Disk Total       :", round(disk.total / (1024 ** 3), 2), "GB")
print("Disk Used        :", round(disk.used / (1024 ** 3), 2), "GB")
print("Disk Free        :", round(disk.free / (1024 ** 3), 2), "GB")
print("Disk Usage       :", disk.percent, "%")

print()
print("========================================")
print("          RESOURCE MONITORING")
print("========================================")

print("CPU Usage        :", cpu_usage, "%")
print("Memory Usage     :", memory.percent, "%")
print("Disk Usage       :", disk.percent, "%")

print("Python Version   :", platform.python_version())

print()
print("========================================")
