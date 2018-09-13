class State:
    def __init__(self, state, toState, read, write, move):
        self.state = state
        self.toState = toState
        self.read = read
        self.write = write
        self.move = move

    def stateInfo(self):
        print('Estado: ',self.state)
        print('Para estado: ',self.toState)
        print('Lendo: ',self.read)
        print('Escreve: ',self.write)
        print('Move: ',self.move)
