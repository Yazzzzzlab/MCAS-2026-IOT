import RPi.GPIO as GPIO
import time

LED_PIN = 11     # 實體腳位 11 (GPIO17)，接 LED
BUZZER_PIN = 12  # 實體腳位 12 (GPIO18)，接蜂鳴器
freq = 523       # 蜂鳴器頻率 (523Hz，大約是 C5)

# 摩斯密碼時間 (秒)
UNIT = 0.2
SHORT = UNIT          # 短 (dot)
LONG = UNIT * 3       # 長 (dash)
SYMBOL_GAP = UNIT     # 同一個字母內，每個短/長之間的間隔
LETTER_GAP = UNIT * 3 # 字母之間的間隔
WORD_GAP = UNIT * 7   # 每次 SOS 之間的間隔

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# 建立 PWM 物件，設定頻率 freq
voice = GPIO.PWM(BUZZER_PIN, freq)


def signal(duration):
    # LED 亮、蜂鳴器響，持續 duration 秒後一起關掉
    GPIO.output(LED_PIN, GPIO.HIGH)
    voice.start(50)   # duty 50%，發聲
    time.sleep(duration)
    GPIO.output(LED_PIN, GPIO.LOW)
    voice.stop()
    time.sleep(SYMBOL_GAP)


def letter(duration):
    # 一個字母 = 三個相同長度的訊號 (S: 三短, O: 三長)
    for _ in range(3):
        signal(duration)
    time.sleep(LETTER_GAP - SYMBOL_GAP)


try:
    while True:
        print("S")
        letter(SHORT)  # 三短
        print("O")
        letter(LONG)   # 三長
        print("S")
        letter(SHORT)  # 三短
        time.sleep(WORD_GAP - LETTER_GAP)

except KeyboardInterrupt:
    pass
finally:
    voice.stop()
    GPIO.cleanup()
