import os
from time import sleep

a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print (a+'\t          TOMBOL TAMBAHAN TERMUX')
print (b+'\t           RYNZ 01')
print ('\t              Rynz-01')
print (a+'+'*40)
try:
     os.mkdir('/data/data/com.termux/files/home/.termux')
except:pass
key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAP','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
fan = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
fan.write(key)
fan.close ()
os.system ('termux-reload-settings')
print (a+'SUCCESSFUL ADDING BUTTONS')

