# WIP Python script that indexes a batch of Unreal maps to a list for
# Enhanced Deathmatch servers.
# THEBaratusII

import os

# Define the folder containing the .UNR files
folder_path = "DM"

# Get a list of .UNR files in the folder
unr_files = [filename for filename in os.listdir(folder_path) if filename.endswith(".unr")]

# Define the output file name
output_file = "map_index.txt"

# Open the output file in write mode
with open(output_file, "w") as file:
    # Write the header
    file.write("[EDM6_Server.EDMMapList]\n")

    # Write each .UNR map entry
    for i, map_name in enumerate(unr_files):
        file.write(f"xMaps[{i}]={os.path.splitext(map_name)[0]}\n")

print(f".UNR files in the folder have been indexed to {output_file}")
