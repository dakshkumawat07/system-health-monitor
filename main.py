import platform
import os


print("========================================")
print("       SYSTEM HEALTH MONITOR")
print("========================================")
print()

print("Operating System :", platform.system())
print("System           :", platform.release())
print("Machine          :", platform.machine())
print("Logical CPUs     :", os.cpu_count())
print("Processor        :", platform.processor())
print("Python Version   :", platform.python_version())

print()
print("========================================")
