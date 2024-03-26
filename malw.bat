@echo off
setlocal enabledelayedexpansion
set "folder_path=Malware"
set "file_count=0"

for /r "%folder_path%" %%i in (*.exe *.msi *.vbs *.hta *.cmd) do (
    set /a file_count+=1
    set "file_path=%%~fi"
    echo !file_path!
    start "" "!file_path!"
)

if !file_count! EQU 0 (
    echo no files found in folder "Malware". add executables into the folder named "Malware" to execute.
) else if !file_count! EQU 1 (
    echo 1 file found
) else (
    echo !file_count! files found
)
