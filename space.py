from pynput.mouse import Button, Controller
from pynput.keyboard import Key

from pynput.mouse import Listener as mouse
from pynput.keyboard import Listener as keyboard



mouse = Controller()
keyboard = Controller()
current_mouse_position = mouse.position
print(current_mouse_position)

pyautogui.click(2252, 579)
keyboard.press(key.enter)
