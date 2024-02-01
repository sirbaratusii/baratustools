# Python script that simply backports a batch of Unreal maps
# to be compatible with 224v/225f

import binascii
import os

def replace_hex_string(file_path, search_hex, replace_hex):
    with open(file_path, 'rb') as file:
        content = bytearray(file.read())

    search_bytes = binascii.unhexlify(search_hex)
    replace_bytes = binascii.unhexlify(replace_hex)

    index = content.find(search_bytes)
    if index != -1:
        while index != -1:
            content[index:index + len(search_bytes)] = replace_bytes
            index = content.find(search_bytes, index + len(replace_bytes))

        new_file_path = file_path.replace('.unr', '_fix.unr')
        with open(new_file_path, 'wb') as new_file:
            new_file.write(content)

        print(f'Modified file saved as: {new_file_path}')
    else:
        print(f'Search hex not found in {file_path}. File not modified.')

def process_unr_files(directory, search_hex, replace_hex):
    for filename in os.listdir(directory):
        if filename.lower().endswith('.unr'):
            file_path = os.path.join(directory, filename)
            replace_hex_string(file_path, search_hex, replace_hex)

if __name__ == "__main__":
    directory_path = input("Enter the path to the directory containing .unr files: ")
    search_hex = "4C6576656C53756D6D617279"
    replace_hex = "5370656369616C4576656E74"

    if os.path.isdir(directory_path):
        process_unr_files(directory_path, search_hex, replace_hex)
    else:
        print("Invalid directory path. Please provide a valid directory containing .unr files.")
