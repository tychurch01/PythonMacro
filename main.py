import time
import keyboard
import pyautogui

'''
python macro reliant on window focus
'''

windowtitle="PROCESSOR NAME"
def action_2(e):
    delay = 0.44 

    def is_correct_window():
        import win32gui
        window_title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        return windowtitle in window_title

    if keyboard.is_pressed('2'):
        if is_correct_window():
            print("Autoclick Enabled")
            while True:
                time.sleep(delay)  
                pyautogui.click(button='left')


                if keyboard.is_pressed('3'): 
                    print("Autoclick Disabled")
                    break

                if not is_correct_window():
                    print("Autoclick Disabled")
                    break 




keyboard.on_press_key('2', action_2)

while True:
    if keyboard.is_pressed('3'):  
        break
    keyboard.wait()  # Wait for any key press
