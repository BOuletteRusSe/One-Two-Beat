
from scipy.io import wavfile
import numpy as np
from time import sleep
from os import system
from colored import attr, fg

def main():
    
    _t = 0
    to_del = []
    is_d = False
    frq = 0
    
    system('@echo off')
    system('color a')
    system('title 1-2-Beat By BOuletteRusSe')
    system('cls')

    while True:

        path = input('%s%sPlease enter the music path (ONLY IN .WAV): ' % (fg(4), attr(1)))

        try: 
            fs, data = wavfile.read(path)
            break
        except: 
            print('%s%sInvalid path !' % (attr(0), fg(1)))
            sleep(1.5)
            system('cls')
            
    while True:
        
        frq = input('%s%sPlease enter the bit cut frequency (10000 -> Fast, 100000 -> Slow): ' % (fg(34), attr(1)))
        
        try:
            frq = int(frq)
            break
        except:
            print('%s%sPlease enter a correct value !' % (attr(0), fg(1)))
            sleep(1.5)
            system('cls')

    for i in enumerate(data):
        
        if _t >= frq: is_d = True
        if _t <= 0: is_d = False
        
        if is_d: 
            _t -= 1
            to_del.append(i[0])
        else: _t += 1

    data = np.delete(data, to_del, 0)
    wavfile.write('result.wav', fs, data)
    
    print('%s%s%sEnded !\nThe file was saved as \"result.wav\" !' % (fg(2), attr(1), attr(4)))
    print('%sPress any key to exit...' % (attr(0)))
    system('pause >nul')

if __name__ == '__main__': main()
