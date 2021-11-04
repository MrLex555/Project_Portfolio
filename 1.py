#%%

import time

#%%

def procedure():
    print(time.asctime())

#%%

def cycle_breaker(triger):
    if triger > 5:
        print('Time to break the cycle')
        return True

#%%

break_triger = 0
while True:
    break_triger += 1
    procedure()
    if cycle_breaker(break_triger):
        break
    time.sleep(1)
