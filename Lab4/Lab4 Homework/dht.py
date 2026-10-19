import time
import board
import adafruit_dht

# DHT11 的 DATA 腳接在 GPIO4（實體腳位 7），接在別的腳就改成對應的 board.Dxx
dhtDevice = adafruit_dht.DHT11(board.D4, use_pulseio=False)

while True:
    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print("Temp:{:.1f} C / {:.1f} F    Humidity: {}%".format(
            temperature_c, temperature_f, humidity))

    except RuntimeError as error:
        # DHT 讀取常常失敗（例如 checksum 錯誤），印出訊息後繼續讀就好
        print(error.args[0])
        time.sleep(2.0)
        continue

    except Exception as error:
        dhtDevice.exit()
        raise error

    except KeyboardInterrupt:
        dhtDevice.exit()
        break

    time.sleep(2.0)
