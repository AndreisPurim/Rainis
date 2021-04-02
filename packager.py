import os
import time
if os.path.isfile('aspazia.py'):
    cwd = os.getcwd()
    os.system("cd "+cwd+ " & pyinstaller --onefile --noconsole aspazia.py")
    print("done!")
else:
    print("aspazia.py not found!")
time.sleep(10)
