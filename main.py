import time
import keyboard
import pyautogui

windowtitle="Roblox"
def action_2(e):
    delay = 0.44  # Set your desired delay for action 2

    def is_correct_window():
        import win32gui
        window_title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        return windowtitle in window_title

    if keyboard.is_pressed('2'):
        if is_correct_window():
            print("Autoclick Enabled")
            while True:
                time.sleep(delay)  # Wait for the specified delay
                pyautogui.click(button='left')

                # Check if the exit key is pressed
                if keyboard.is_pressed('3'):  # Replace 'esc' with your desired exit key
                    print("Autoclick Disabled")
                    break

                # Check if Roblox window loses focus (new window selected)
                if not is_correct_window():
                    print("Autoclick Disabled")
                    break  # Exit the loop if not Roblox window




keyboard.on_press_key('2', action_2)
# Check for exit key in the main loop
while True:
    if keyboard.is_pressed('3'):  # Replace 'esc' with your desired exit key
        break
    keyboard.wait()  # Wait for any key press
