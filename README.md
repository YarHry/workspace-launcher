# Windows Workspace Launcher
A lightweight CLI utility written in Python to instantly open your daily development, music, or browsing workspaces with a single keypress.

<img width="1851" height="765" alt="image" src="https://github.com/user-attachments/assets/913f58c6-38e9-4739-ad57-6985e382e19b" />



### Features
Instant Input: Uses msvcrt.getch() for immediate response without pressing Enter.

Borderless UI: Automatically stretches the console window to fullscreen using the Windows API (ctypes).

Custom Profiles: Quick switching between work, music production (DAW + tabs), and programming environments.

Aesthetic CLI: Styled with custom ASCII banners and ANSI colors.


### Tech Stack
Language: Python 3.x

Platform: Windows-only (msvcrt, ctypes)

Dependencies: Standard library only (no pip install required)


### Configuration
Before running the script, open launcher.py and update the absolute paths to match your local setup:

subprocess.Popen(r"C:\Your\Path\To\App.exe")


### Customizing Banners
Banners in the script were generated using the Alligator2 font on [TAAG](https://patorjk.com/software/taag). You can generate your own text, paste it into the banner variables, and apply any ANSI color(you can find a lot of them in the code).


### Run on Windows Startup (Optional)
If you want the launcher to open automatically when you boot your PC:

1. Create a start_launcher.bat file:

  @echo off

  cls

  python "C:\Users\yarik\Desktop\Workspace Launcher.py"

  exit

2. Press Win + R, type shell:startup, and press Enter.

3. Move a shortcut of your .bat file into that folder.


### Usage
In Bash:

git clone [https://github.com/YarHry/workspace-launcher.git](https://github.com/YarHry/workspace-launcher.git)

cd workspace-launcher

python launcher.py
