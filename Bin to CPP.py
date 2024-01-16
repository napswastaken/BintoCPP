import os
import subprocess

# Define the folder to search for config.bin files, example 'P:\NULLED_SERVER'
folder_path = r'PathToYourModFolder'

# Path to the BINToCPP.bat script, assumes default install location
batch_script_path = r'C:\Program Files (x86)\Steam\steamapps\common\DayZ Tools\Bin\CfgConvert\BINToCPP.bat'


def process_config_bin(config_bin_file):
    command = [batch_script_path, config_bin_file]

    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully processed {config_bin_file}")

        os.remove(config_bin_file)  # remove the .bin file after converting it to a config.cpp, I don't see a reason to keep it?
    except subprocess.CalledProcessError as e:
        print(f"Error processing {config_bin_file}: {e}")


for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.lower() == 'config.bin':
            config_bin_file_path = os.path.join(root, file)
            process_config_bin(config_bin_file_path)