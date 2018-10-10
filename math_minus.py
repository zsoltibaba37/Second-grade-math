#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import random, sys, shutil, os, time
#import winsound

# Jó az eredmény - Hangjelzés
freq = 1000
dur = 250
# Nemjó az eredmény - Hangjelzés
freqn = 500
durn = 300
y = 4

a = int()
b = int()
c = int()
d = int()

os.system('clear')
print ("-" * 80)
print (" Szia Milán :-) ")
print (" Gyakoljunk egy kis kivonást. ")
print ("-" * 80)

while True:
    if a > 0:
        if bal == jobb:
            print("-" * 80)
            print("A megadott szám jó !")
            print ( bal, "=", jobb, )
            print( a, " - ", "[", d, "]", " = ", b, " - ", c)
            print("-" * 80)
            #winsound.Beep(freq, dur)
            #        winsound.PlaySound("*", winsound.SND_ALIAS)
            #        time.sleep(0.5)
            print("A Programból való kilépéshez nyomd meg a CTRL-C billentyű kombinációt")
        else:
            print("-" * 80)
            print("A megadott szám nemjó !")
            print("A helyes szám =", "[", a - (b - c) , "]")
            print(a, " - ", "[", a - (b - c), "]", " = ", b, " - ", c)
            print("-" * 80)
            #winsound.Beep(freqn, durn)
            #        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
            #        time.sleep(0.5)
            print("A Programból való kilépéshez nyomd meg a CTRL-C billentyű kombinációt")
    else:
        pass

    a = random.randrange(11, 20)
    b = random.randrange(9, 16)
    c = random.randrange(1, 7)

    print ("-" * 80)
    print (a, "- [  ] = ", b, "-", c)
    print ("-" * 80)

    while True:
        try:
            d = int(input("Mennyi a hiányzó szám értéke? : "))
#            if d < 0:
#               d = 0
#            else:
#                pass
#            z = y / d
            break
        except ValueError:
            print("Ez nem egy szám, vagy nem egész érték lett megadva!")  # A belovasott érték valóban egész szám?
#        except ZeroDivisionError:
#            print("A megadott érték nulla vagy negatív!")  # A beolvasott érték nem lehet nulla
        except KeyboardInterrupt:  # control-c -re kilép a programból
            sys.exit(0)
    bal = a - d
    jobb = b - c
    #
    os.system('clear')
#    os.system('cls')
