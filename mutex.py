mutex: int = 0
    
def lock():
    while mutex == 1:
        pass
    mutex = 1
    
def unlock():
    mutex = 0
    
'''
Problem:
If cpu interupt or on multi-core cpu:
thread 1                | thread 2
call "while mutex == 1" |
break the while         |
****interupted***       |
                        | call "while mutex == 1" 
                        | break the while
                        | set mutex = 1
                        | continue in thread 
                        | ***interupted***
continue in thread      |
-> Race condition

To solve this, need a special atomic instruction, it will look like this (psuedo code):
def testAndSet(old_pointer: int*, new_value: int) -> int:
    old_value: int = *old_pointer
    *old_pointer = new_value
    return old_value
    
and will be use like this:
def lock():
    while testAndSet(&lock, 1) == 1:
        pass
'''
