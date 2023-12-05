import time              # python自带 不用安装
import pyautogui                        # pip install pyautogui
import ctypes
import sys
import keyboard
def mainLoop():
    time.sleep(2)
    pyautogui.press("Y")
    #按下Y键
    time.sleep(0.4)
    pyautogui.moveTo(1195, 372, duration=0) #拒绝按钮所在位置
#                    点击时间，坐标
    time.sleep(0.5)
    pyautogui.click()   #点击同意按钮
    print("拒绝申请完毕！")

if __name__ == '__main__':
    # 判断当前进程是否以管理员权限运行
    if ctypes.windll.shell32.IsUserAnAdmin() :
        print('当前已是管理员权限')
        mainLoop()
    else:
        print('当前不是管理员权限，以管理员权限启动新进程...')
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)