# -*- coding: utf-8 -*-
from shutil import copy
from os import listdir, rename
from os.path import isdir

#This old version is worse than the other pls don't use

# The destiny folder you want your .mp3's to be copied
dst = ''

# Your osu! songs folder
songs = 'D:\\osu!\\Songs'
audio = []
num = 1

for f in listdir(songs):
    src = songs + '\\' + f

    if (isdir(src)):
        for i in listdir(src):
            name = i.split('.')

            if (name[-1] == 'mp3'):
                mp3 = src + '\\' + i

                if (i in audio):
                    name[-2] += (str(num) + '.')
                    ren = ''.join(name)
                    aux = src + '\\' + ren

                    rename(mp3, aux)
                    audio.append(ren)
                    copy(aux, dst)
                    rename(aux, mp3)

                    num+=1
                else:
                    audio.append(i)
                    mp3 = src + '\\' + i
                    copy(mp3, dst)

audio.sort()
print(audio)
