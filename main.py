#!/usr/bin/env python3
import random
import argparse

# если есть аргумент при вызове, то выводим сторону монетки
# если нет, то спрашиваем что хочет сделать пользователь с монеткой

class Coin:
    def __init__(self):
        self.value = False
        self.flip = False
    def get_flip(self):
        self.flip = True
        res_flip = random.randint(0,1)
        if (res_flip):
            self.value = "ОРЕЛ"
        else:
            self.value = "РЕШКА"
    def see_res_flip(self):
        if (self.flip):
            print ("Вам выпал:   " + self.value)
            self.flip = False
        else:
            print("\nСначала подбросьте монетку!\n")

def main():
    parser = argparse.ArgumentParser(description='Указываем количество бросков через --с=N')
    parser.add_argument("--c", default=0)  # количество бросков
    args = parser.parse_args()
    count = args.c
    coin = Coin()
    if (count):
        for n in range(int(count)):
            Coin.get_flip(coin)
            Coin.see_res_flip(coin)
    else :
        while True:
            userinput = input("Выберите ваше действие:\n"
            + "1 - подбросить монетку\n"
            + "2 - посмотреть результат\n"
            + "любая другая клавиша - выход из программы\n")
            if (userinput == '1'):
                Coin.get_flip(coin)
            elif (userinput == '2'):
                print()
                Coin.see_res_flip(coin)
                print()
            else:
                break

main()