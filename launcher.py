""" Workspace Launcher """

import ctypes
import os
import msvcrt
import webbrowser
import subprocess

# Remove the border and force the window to refresh/expand to full screen
try:
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd:
        GWL_STYLE = -16
        style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_STYLE)
        
        # Remove the header, resize bar, and system menu
        style &= ~0x00C00000  # WS_CAPTION
        style &= ~0x00040000  # WS_THICKFRAME
        style &= ~0x00080000  # WS_SYSMENU
        ctypes.windll.user32.SetWindowLongW(hwnd, GWL_STYLE, style)
        
        # We retrieve the screen dimensions and immediately resize the window 
        user32 = ctypes.windll.user32
        screen_width = user32.GetSystemMetrics(0)
        screen_height = user32.GetSystemMetrics(1)
        
        user32.SetWindowPos(hwnd, 0, 0, 0, screen_width, screen_height, 0x0004 | 0x0020 | 0x0040)
except Exception:
    pass

os.system('')


music_list = ["https://www.songsterr.com/", "https://www.youtube.com/", "https://open.spotify.com/", "https://gemini.google.com/app?hl=ru"]
programming_list = ["https://stepik.org/course/58852/syllabus", "https://www.codewars.com/", "https://monkeytype.com/", "https://open.spotify.com/", "https://gemini.google.com/app?hl=ru",]

#colors
RESET = "\033[0m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"


banner1 = """






   :::                           :::       :::  ::::::::  :::::::::  :::    :::       :::::::           ::::::::  :::    ::: ::::::::::: :::        :::		 
 :+:+:                           :+:       :+: :+:    :+: :+:    :+: :+:   :+:       :+:   :+:         :+:    :+: :+:    :+:     :+:     :+:        :+:       
   +:+                           +:+       +:+ +:+    +:+ +:+    +:+ +:+  +:+         +:+ +:+          +:+        +:+    +:+     +:+     +:+        +:+       
   +#+        +#++:++#++:++      +#+  +:+  +#+ +#+    +:+ +#++:++#:  +#++:++           +#++:  ++#      +#+        +#++:++#++     +#+     +#+        +#+       
   +#+                           +#+ +#+#+ +#+ +#+    +#+ +#+    +#+ +#+  +#+         +#+ +#+#+#       +#+        +#+    +#+     +#+     +#+        +#+       
   #+#                            #+#+# #+#+#  #+#    #+# #+#    #+# #+#   #+#       #+#   #+#+        #+#    #+# #+#    #+#     #+#     #+#        #+#       
 #######                           ###   ###    ########  ###    ### ###    ###       ##########        ########  ###    ### ########### ########## ########## 

"""
banner2 = """

  ::::::::                          ::::    ::::  :::    :::  :::::::: ::::::::::: ::::::::  
 :+:    :+:                         +:+:+: :+:+:+ :+:    :+: :+:    :+:    :+:    :+:    :+: 
       +:+                          +:+ +:+:+ +:+ +:+    +:+ +:+           +:+    +:+        
     +#+         +#++:++#++:++      +#+  +:+  +#+ +#+    +:+ +#++:++#++    +#+    +#+        
   +#+                              +#+       +#+ +#+    +#+        +#+    +#+    +#+        
  #+#                               #+#       #+# #+#    #+# #+#    #+#    #+#    #+#    #+# 
 ##########                         ###       ###  ########   ######## ########### ########  

"""
banner3 = """

  ::::::::                          :::::::::  :::::::::   ::::::::   ::::::::  :::::::::      :::     ::::    ::::: ::::    ::::: ::::::::::: ::::    :::  :::::::: 
 :+:    :+:                         :+:    :+: :+:    :+: :+:    :+: :+:    :+: :+:    :+:   :+: :+:   +:+:+: :+:+:+ +:+:+: :+:+:+     :+:     :+:+:   :+: :+:    :+:
        +:+                         +:+    +:+ +:+    +:+ +:+    +:+ +:+        +:+    +:+  +:+   +:+  +:+ +:+:+ +:+ +:+ +:+:+ +:+     +:+     :+:+:+  +:+ +:+       
     +#++:       +#++:++#++:++      +#++:++#+  +#++:++#:  +#+    +:+ :#:        +#++:++#:  +#++:++#++: +#+  +:+  +#+ +#+  +:+  +#+     +#+     +#+ +:+ +#+ :#:       
        +#+                         +#+        +#+    +#+ +#+    +#+ +#+   +#+# +#+    +#+ +#+     +#+ +#+       +#+ +#+       +#+     +#+     +#+  +#+#+# +#+   +#+#
 #+#    #+#                         #+#        #+#    #+# #+#    #+# #+#    #+# #+#    #+# #+#     #+# #+#       #+# #+#       #+#     #+#     #+#   #+#+# #+#    #+#
  ########                          ###        ###    ###  ########   ########  ###    ### ###     ### ###       ### ###       ### ########### ###    ####  ######## 

"""

print("\033[H\033[J", end="")#clears the console

print(LIGHT_CYAN + banner1 + RESET)
print(LIGHT_PURPLE + banner2 + RESET)
print(LIGHT_BLUE + banner3 + RESET)


while True:
	char = msvcrt.getch()
	try:
		mode = char.decode('utf-8')
	except UnicodeDecodeError:
		mode = char.decode('cp1251', errors='ignore')


	#chill&work
	if mode == "1":
		subprocess.Popen(r"C:\Your\Path\To\App.exe")
		subprocess.Popen([r"C:\Program Files\Google\Chrome\Application\chrome.exe", "--restore-last-session"])
		break

	#music
	elif mode == "2":
		os.startfile(r"C:\Your\Path\To\App.exe")
		for url in music_list:
			webbrowser.open_new_tab(url)
		break

	#programming
	elif mode == "3":
		subprocess.Popen(r"C:\Your\Path\To\App.exe")
		for url1 in programming_list:
			webbrowser.open_new_tab(url1)
		break

	elif mode == "0":
		break