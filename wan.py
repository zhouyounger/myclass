import os,sys
from time import sleep


def f1():
    sleep(3)
    print('事件1')

def f2():
    sleep(4)
    print('事情2')

pid = os.fork()

if pid<0:
    print('Error')
elif pid == 0:
    p = os.fork()
    if p == 0 :
        f2()
    else:
        os._exit(0)
else:
    os.wait()
    f1()
    
    