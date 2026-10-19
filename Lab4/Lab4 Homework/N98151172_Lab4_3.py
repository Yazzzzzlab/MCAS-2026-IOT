import serial
import time

# 開啟 UART，/dev/serial0 會指向樹莓派 GPIO14/15 的序列埠
ser = serial.Serial("/dev/serial0", baudrate=9600, timeout=1)

try:
    print("UART loopback 測試，按 Ctrl+C 可以停止...")
    count = 0

    while True:
        message = "Hello UART {}\n".format(count)

        # 送出資料（要轉成 bytes）
        ser.write(message.encode("utf-8"))
        print("送出:", message.strip())

        # 讀回一行資料（TX 接 RX，所以會收到自己送的內容）
        received = ser.readline().decode("utf-8").strip()
        if received:
            print("收到:", received)
        else:
            print("沒有收到資料，請檢查 TX 和 RX 是否有接在一起")

        count += 1
        time.sleep(1)

except KeyboardInterrupt:
    print("\n停止測試...")

finally:
    ser.close()
    print("UART 已關閉，程式結束。")
