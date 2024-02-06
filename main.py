import pyautogui
import keyboard

def perform_action(move_y):
    pyautogui.click(button='right')
    pyautogui.move(0, move_y, duration=0.15)
    pyautogui.click(button='left')
    pyautogui.move(0, -move_y, duration=0.10)

def action_1(e):
    perform_action(115)


# bind the actions to the '1' and '2' keys
keyboard.on_press_key('1', action_1)

# start the event loop
keyboard.wait()