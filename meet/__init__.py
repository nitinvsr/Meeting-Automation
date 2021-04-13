import pyautogui
import schedule
import time

def enter_meet(def_browser,url):
    #I open your browser and enter your url
    pyautogui.press('win',interval=0.5)
    pyautogui.write(def_browser)
    time.sleep(3)
    pyautogui.press('enter',interval=0.5)
    time.sleep(10)
    pyautogui.press('enter',interval=0.5)
    pyautogui.write(url)
    pyautogui.press('enter',interval=0.5)
    time.sleep(10)
    
    #I switch off your audio and video
    pyautogui.hotkey('ctrl','e')
    pyautogui.hotkey('ctrl','d')
    
    #I finally join you to the meet
    join_btn=pyautogui.locateOnScreen('./Capture.png')
    pyautogui.press('enter',interval=0.5)
    print(join_btn)
    join_btn=pyautogui.center(join_btn)
    print(join_btn)
    pyautogui.click(join_btn.x, join_btn.y)
    print(join_btn.x,join_btn.y)    