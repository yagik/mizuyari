#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

#GPIO.setmode(GPIO.BCM)

#PIN1 = 14
#PIN2 = 15

#GPIO.setup(PIN1,GPIO.OUT)
#GPIO.setup(PIN2,GPIO.OUT)

def main ():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    PIN1 = 14
    PIN2 = 15

    GPIO.setup(PIN1,GPIO.OUT)
    GPIO.setup(PIN2,GPIO.OUT)

    while True:
        print("やりたい事を選んで")
        print("1. 水をやる")
        print("2. バルブを開ける")
        print("3 バルブを閉める")
        print("4. 時間指定で水をやる")
        print("5. 終了する")


        choice = input("選択肢を入力してください:")

        if choice == "1":
            print("Valve Open")
            GPIO.output(PIN1, True)
            GPIO.output(PIN2, False)
            time.sleep(10)

            print("Valve Close")
            GPIO.output(PIN1, False)
            GPIO.output(PIN2, True)

            print("GPIO off")
            GPIO.output(PIN1,False)
            GPIO.output(PIN2,False)
            GPIO.cleanup()

        elif choice == "2":
            print("Valve Open")
            GPIO.output(PIN1, True)
            GPIO.output(PIN2, False)
            print("ちゃんと閉じてね")

        elif choice == "3":
            print("Valve Close")
            GPIO.output(PIN1, False)
            GPIO.output(PIN2, True)
            time.sleep(1)

            GPIO.output(PIN2, False)
            GPIO.cleanup()

        elif choice == "4":
            print("時間を秒で教えてね")
            zikan = int(input())
            print("Valve Open")
            GPIO.output(PIN1, True)
            GPIO.output(PIN2, False)
            time.sleep(zikan)

            print("Valve Close")
            GPIO.output(PIN1, False)
            GPIO.output(PIN2, True)

            print("GPIO off")
            GPIO.output(PIN1,False)
            GPIO.output(PIN2,False)
            GPIO.cleanup()


        elif choice == "5":
            print("終わります")
            break

        else:
            print("\n選択肢の中から選んでくださいね\n")



if __name__ == "__main__":
    main()

