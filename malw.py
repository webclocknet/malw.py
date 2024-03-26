import os
import subprocess
import sys

def execute_files(folder_path):
    file_paths = set()
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(('.exe', '.msi', '.vbs', '.hta', '.cmd')):
                file_path = os.path.abspath(os.path.join(root, file))
                file_paths.add(file_path)
    
    if len(file_paths) == 0:
        print('No files found in folder "Malware". Add executables into the folder named "Malware" to execute.')
    elif len(file_paths) == 1:
        print(f"{len(file_paths)} file found")
    else:
        print(f"{len(file_paths)} files found")
    processes = []
    for file_path in file_paths:
        print(f"{file_path}")
        process = subprocess.Popen([file_path], shell=True)
        processes.append(process)
    
    for process in processes:
        process.wait()

if __name__ == "__main__":
    execute_files("Malware")
