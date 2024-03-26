import os
import subprocess
import sys
import ctypes

def is_admin():
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

def execute_files(folder_path):
    file_paths = set()
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(('.exe', '.msi', '.vbs', '.hta', '.cmd')):
                file_path = os.path.abspath(os.path.join(root, file))
                file_paths.add(file_path)
    
    if len(file_paths) == 0:
        print('no files found in folder "Malware". add executables into the folder named "Malware" to execute.')
    elif len(file_paths) == 1:
        print(f"{len(file_paths)} file found")
    else:
        print(f"{len(file_paths)} files found")
    processes = []
    for file_path in file_paths:
        print(f"{file_path}")
        if is_admin():
            process = subprocess.Popen([file_path], shell=True)
            processes.append(process)
    
    for process in processes:
        process.wait()
    
    sys.exit()

if __name__ == "__main__":
    if not is_admin():
        if sys.platform == "win32":
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        else:
            sys.exit()
    
    execute_files("Malware")
