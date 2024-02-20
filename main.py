# Author: NeuralNine
import platform
import psutil
import cpuinfo

print(f"Architecture: {platform.architecture()}")
print(f"Network Name: {platform.node()}")
print(f"Operating System: {platform.platform()}")
print(f"Processor: {platform.processor()}")

my_cpuinfo = cpuinfo.get_cpu_info()

print(f"Full CPU Name: {my_cpuinfo['brand_raw']}")
print(f"Full CPU Name: {my_cpuinfo['hz_actual_friendly']}")
print(f"Full CPU Name: {my_cpuinfo['hz_advertised_friendly']}")

print(f"Total RAM: {psutil.virtual_memory().total / 1024 / 1024 / 1024:.2f} GB")