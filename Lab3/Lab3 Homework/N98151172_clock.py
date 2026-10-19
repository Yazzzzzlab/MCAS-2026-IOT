import os
import sys
import time
from datetime import datetime

# 引用 7segment_display/raspberrypi-tm1637 裡的 tm1637.py
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "..", "7segment_display", "raspberrypi-tm1637"))
import tm1637

CLK = 23     # 實體腳位 16 = BCM GPIO23
DIO = 24     # 實體腳位 18 = BCM GPIO24

tm = tm1637.TM1637(clk=CLK, dio=DIO)

try:
    while True:
        now = datetime.now()
        # 每秒的前半秒冒號亮，後半秒冒號暗 → 冒號一秒閃一下
        colon = now.microsecond < 500000
        tm.numbers(now.hour, now.minute, colon)  # 顯示 時:分
        # 睡到下一個半秒，讓冒號切換對齊秒數
        time.sleep(0.5 - (now.microsecond % 500000) / 1000000)

except KeyboardInterrupt:
    pass
finally:
    tm.write([0, 0, 0, 0])  # 結束時清空顯示器
