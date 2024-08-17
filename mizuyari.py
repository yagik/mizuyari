#!/usr/bin/env python3

def mizuyari():
    print ("水やり用のプログラム 作成中...")

def main ():
    while True:
        print("やりたい事を選んで")
        print("1. 水をやる")
        print("2. 何か他の機能")
        print("3. 終了する")


        choice = input("選択肢を入力してください:")

        if choice == "1":
            print("\nここに水やり用のプログラムを書いてね\n")

        elif choice == "2":
            print("\nここに何か他の機能用のプログラムを書いてね\n")

        elif choice == "3":
            print("\nプログラムを終了します\n")
            break

        else:
            print("\n選択肢の中から選んでくださいね\n")



if __name__ == "__main__":
    main()

