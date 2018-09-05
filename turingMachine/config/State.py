from enum import IntEnum

class StateConfig(IntEnum):
    atState = 0
    toState = 1
    read = 2
    write = 3
    move = 4
