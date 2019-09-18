# -*- coding: utf-8 -*-
from shutil import copy
from os import listdir, rename
from os.path import isdir

# The destiny folder you want your .mp3's to be copied
dst = ''

# Your osu! songs folder
songs = 'D:\\osu!\\Songs'
audio = []
num = 1

#this list is supposed to be bigger...
hitsounds = ['normal-hit',
             'soft-hit',
             'drum-hit',
             'applause',
             'combobreak',
             'failsound',
             'sectionfail',
             'sectionpass']

for f in listdir(songs):
    folder = f.split(' ')
    src = songs + '\\' + f

    if (isdir(src)):
        for i in listdir(src):
            name = i.split('.')

            if (name[-1] == 'mp3' and not(name[0].startswith(tuple(hitsounds)))):
                mp3 = src + '\\' + i

                if (i in audio):
               
                    try:
                        if(int(folder[0])):
                            folder.pop(0)
                            folder.append('.mp3')
                            
                            if((' '.join(folder)) in audio):
                                folder.insert(-1, str(num))
                                #Songs with alr used filenames
                                #print(folder)
                                num+=1                                
                            
                            ren = ' '.join(folder)
                            aux = src + '\\' + ren
                                
                            rename(mp3, aux)
                            audio.append(ren)
                            copy(aux, dst)
                            rename(aux, mp3)
                        
                    except ValueError:
                        folder.append('.mp3')
                        
                        ren = ' '.join(folder)
                        aux = src + '\\' + ren
                        
                        rename(mp3, aux)
                        audio.append(ren)
                        copy(aux, dst)
                        rename(aux, mp3)
                    
                else:
                    audio.append(i)
                    mp3 = src + '\\' + i
                    copy(mp3, dst)

audio.sort()
print(audio)
print("Total of scanned mp3s: ", len(audio))
