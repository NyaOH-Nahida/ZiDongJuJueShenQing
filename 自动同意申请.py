#作者：氢氧化喵_NyaOH

import cv2                              # pip install opencv-python
import numpy                            # pip install numpy
from PIL import ImageGrab               # pip install pillow
import pyautogui
import sys, time, ctypes                # python自带 不用安装
from random import random               # python自带 不用安装
import keyboard

print('按F12开始程序...')
keyboard.wait('f12')
img_templ = cv2.imread('friend.jpg') #加载模板图片
THRESHOLD = 0.96 #相似度设定最小为-1，最大为1
#random_number=random.uniform(0.2, 1)#有BUG，注释掉

def mainLoop():
    #截图
    img_src = ImageGrab.grab( bbox=(527, 317, 892, 427)) # x1, y1, x2, y2   80.45.110.85
    img_src.save("截图.jpg") # 调试用
    img_src = cv2.cvtColor(numpy.asarray(img_src), cv2.COLOR_RGB2BGR)

    #模板匹配
    result = cv2.matchTemplate(img_src, img_templ, cv2.TM_CCOEFF_NORMED)
    min_max = cv2.minMaxLoc(result)  #计算匹配度
    print('result.min_max:', min_max)

    # 如果匹配度很高，则认为是好友，于是自动同意申请
    if min_max[1] > THRESHOLD :
        print('是好友，允许加入，待用户确认...')
        time.sleep(0.05 + 0.1 * random())
        # pyautogui.moveTo(1327, 372, duration=0.5)  # 同意按钮所在位置（随机移动时间反检测）
    else:
        print('不是好友，已自动拒绝加入')
        time.sleep(0.05 + 0.1 * random())
        pyautogui.moveTo(1195, 372, duration=0.2)  # 同意按钮所在位（随机移动时间反检测）

if __name__ == '__main__':
    # 判断当前进程是否以管理员权限运行
    if ctypes.windll.shell32.IsUserAnAdmin() :
        print('当前已是管理员权限')
        while True:
            mainLoop()
            pyautogui.press("Y")   #周期按下Y键
            time.sleep(0.3 + 0.2 * random())
    else:
        print('当前不是管理员权限，以管理员权限启动新进程...')
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
