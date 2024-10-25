import os

# You need extract all files from the rom and put them in a single folder
folder_path = '/storage/emulated/0/Download/'

commands = []
first_command = True

# Dictionary to map specific filenames!!
specific_files = {

    "NON-HLOS.bin": "APNHLOS",
    "dspso.bin": "DSP",
    "km41.mbn": "KEYMASTER",
    "qupv3fw.elf": "QUPFW",
    "uefi_sec.mbn": "UEFISECAPP",
    "sec.elf": "SECDATA",
    "vaultkeeper.mbn": "VK",
    "tz_iccc.mbn": "TZICCC",
    "tz_hdm.mbn": "HDM",
    
    # Add more "filename: PARTITION" pairs as needed
}

for filename in os.listdir(folder_path):
    full_path = os.path.join(folder_path, filename)
    if os.path.isfile(full_path):
        if filename in specific_files:
            name_to_use = specific_files[filename]
        else:
            # Remove the file extension and convert to uppercase
            name_to_use = os.path.splitext(filename)[0].upper()
        
        if first_command:
            # Add "heimdall flash" only for the first command
            command = f"heimdall flash --{name_to_use} {full_path}"
            first_command = False  # Set flag to False after the first command
        else:
            # Command without "heimdall flash" for the remaining files
            command = f"--{name_to_use} {full_path}"
        
        commands.append(command)

# Add the final options to the last command
if commands:
    commands[-1] += " --skip-size-check --no-reboot"
print(' '.join(commands))
