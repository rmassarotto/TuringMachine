class TuringMachine:
    def __init__(self, entranceAlphabet, tapeAlphabet, blankSimbol, states, startState, endStates, tapeNumber, transitions):
        self.entranceAlphabet = entranceAlphabet
        self.tapeAlphabet = tapeAlphabet
        self.blankSimbol = blankSimbol
        self.states = states
        self.startState = startState
        self.endStates = endStates
        self.tapeNumber = tapeNumber
        self.transitions = transitions

    def turingMachineInfo(self):
        print('Alfabeto de Entrada: ',self.entranceAlphabet)
        print('Alfabeto da Fita: ',self.tapeAlphabet)
        print('Simbolo Vazio: ',self.blankSimbol)
        print('Estados: ',self.states)
        print('Estado Inicial: ',self.startState)
        print('Estado Final: ',self.endStates)
        print('Numero de Fitas: ',self.tapeNumber)
        #print('Transições: ',*self.transitions, sep = '\n')
        print('Transições: ',self.transitions)

    
