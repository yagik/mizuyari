# Line Notify test

import smbus
import time
import datetime
import requests
import csv

# I2C設定
i2c = smbus.SMBus(1)
address = 0x38

#トリガ設定コマンド
set = [0xAC, 0x33, 0x00]

#データ読み込み用
dat = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

# DHT20/AHT25設定
time.sleep(0.1)
ret = i2c.read_byte_data(address, 0x71)

# トリガ測定コマンド送信
time.sleep(0.01)
i2c.write_i2c_block_data(address, 0x00, set)
    
# データの読み込み
time.sleep(0.08)
dat = i2c.read_i2c_block_data(address, 0x00, 0x07)
    
# データ変換
hum = dat[1] << 12 | dat[2] << 4 | ((dat[3] & 0xF0) >> 4)
tmp = ((dat[3] & 0x0F) << 16) | dat[4] << 8 | dat[5]
    
# 物理量変換
hum = hum / 2**20 * 100
hum = round (hum, 1)     #h
    
tmp = tmp / 2**20 * 200 - 50
tmp = round (tmp, 1)

# Record CSV
dt = datetime.datetime.now()

with open("/home/toshi/Desktop/temp_humidity_log.csv","a") as f:
    writer = csv.writer(f)
    writer.writerow([dt.strftime("%Y-%m-%d"), dt.strftime("%H:%M"), tmp, hum])


'''
# 表示
print("Humidity is: " + str(hum) + "%")
print("Temparature is: " + str(tmp) + " degrees Celcius" )
'''

#For Line code, let it comment out for a while
#---Code for using Line Notify---#
# Line notify token
# 7M95tQfRNcYT6PKyhdkm4MZhcTWzSNogwe4fZNwlR2H

'''
ACCESS_TOKEN = "7M95tQfRNcYT6PKyhdkm4MZhcTWzSNogwe4fZNwlR2H"
headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

tmp_now = ("Temparature is: " + str(tmp) + " degrees Celcius desuyo." )

data = {"message": f" {tmp_now}" }

requests.post(
    "https://notify-api.line.me/api/notify",
    headers=headers,
    data=data
)
'''    