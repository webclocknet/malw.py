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
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(('.exe', '.msi', '.vbs', '.hta', '.cmd')):
                file_path = os.path.join(root, file)
                file_paths.append(file_path)
    
    print(f"{len(file_paths)} files found")
    for file_path in file_paths:
        print(f"{file_path}")
        subprocess.call([file_path], shell=True)

if __name__ == "__main__":
    if not is_admin():
        print("enable admin privileges? (y/n)")
        response = input().lower()
        if response == 'y':
            if sys.platform == "win32":
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            else:
                print("Run this script as admin.")
                sys.exit()
        else:
            print("exit")
            sys.exit()
    
    execute_files("Malware")
