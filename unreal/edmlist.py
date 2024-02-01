# Python script that indexes a batch of Unreal maps to a list for
# Enhanced Deathmatch servers.
# THEBaratusII

import os

# Ask the user for the folder path
folder_path = input("Enter the path to the folder containing .unr files: ")

# Validate the folder path
while not os.path.isdir(folder_path):
    print("Invalid folder path. Please provide a valid directory.")
    folder_path = input("Enter the path to the folder containing .unr files: ")

# Get a list of .unr files in the folder
unr_files = [filename for filename in os.listdir(folder_path) if filename.lower().endswith(".unr")]

# Define the output file name
output_file = "EDMMAPS.ini"

# Open the output file in write mode
with open(output_file, "w") as file:

    # Write [EDM6_Server.EDMMapList]
    file.write("[EDM6_Server.EDMMapList]\n")

    # Write each .unr map entry
    for i, map_name in enumerate(unr_files):
        file.write(f"xMaps[{i}]={os.path.splitext(map_name)[0]}\n")
        
    # Write dummy xMaps entries up to 999 if there are not enough .unr files
    for i in range(len(unr_files), 1000):
        file.write(f"xMaps[{i}]={os.path.splitext('')[0]}\n")

    # Write xMapNum
    file.write("xMapNum=1\n")

    # Write dummy Maps entries up to 31
    for i in range(1, 32):
        file.write(f"Maps[{i}]={os.path.splitext('')[0]}\n")

    # Write dummy MapNum
    file.write("MapNum=0\n")
    
    # Write bShuffleMaps
    file.write("bShuffleMaps=True\n")


print(f".unr files in the folder have been indexed to {output_file}")
