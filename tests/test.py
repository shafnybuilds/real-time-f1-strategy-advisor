import os

# get current dir
current_dir_abs = os.path.dirname(os.path.abspath(__file__))
print(f"Absolute Path: {current_dir_abs}")

current_dir_real = os.path.dirname(os.path.realpath(__file__))
print(f"Real Path: {current_dir_real}")