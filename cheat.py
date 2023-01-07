from pynput.keyboard import Key, Controller
import win32clipboard
import time


klavye = Controller()
time.sleep(1)
klavye.press(Key.ctrl)
klavye.press(Key.alt)
klavye.press(Key.shift)
klavye.press("m")
klavye.release(Key.ctrl)
klavye.release(Key.alt)
klavye.release(Key.shift)
klavye.release("m")
time.sleep(4)
win32clipboard.OpenClipboard()
yazi = win32clipboard.GetClipboardData().replace("\n", " ")
win32clipboard.CloseClipboard()
klavye.type(yazi)
