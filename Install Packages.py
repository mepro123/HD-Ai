import subprocess
import sys
import os

packages = [
    "opencv-python",
    "torch",
    "torchvision",
    "torchaudio",
    "seaborn",
    "ultralytics",
    "mss",
    "PyQt5",
    "pywin32",
    "Keyboard"
]

def install_package(package):
    print(f"Installing {package} ...")

    CREATE_NO_WINDOW = 0x08000000  # Windows flag to hide console window

    cmd = [sys.executable, "-m", "pip", "install", package]

    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        bufsize=1,
        creationflags=CREATE_NO_WINDOW if os.name == 'nt' else 0
    )

    # Read line by line to show live output (including progress)
    while True:
        output = proc.stdout.readline()
        if output == '' and proc.poll() is not None:
            break
        if output:
            print(output.strip())
    retcode = proc.poll()

    if retcode == 0:
        print(f"Finished installing {package}\n")
    else:
        print(f"Error installing {package} (code {retcode})\n")

def main():
    for pkg in packages:
        install_package(pkg)

    print("All packages installed. Press Enter to exit.")
    input()

if __name__ == "__main__":
    main()
