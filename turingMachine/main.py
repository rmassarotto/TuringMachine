from model.TuringMachine import TuringMachine
from model.Tape import Tape
from model.State import State
from config.TuringMachine import MachineConfig
from config.State import StateConfig

configFile = open('abc.txt', 'r').read().splitlines()
tapeData = list('BaabbccB')

tape = Tape(tapeData, 1, tapeData[1])
turing = TuringMachine(
    configFile[MachineConfig.entranceAlphabet],
    configFile[MachineConfig.tapeAlphabet],
    configFile[MachineConfig.blankSimbol],
    configFile[MachineConfig.states],
    configFile[MachineConfig.startState],
    configFile[MachineConfig.endStates],
    configFile[MachineConfig.tapeNumber],
    configFile[MachineConfig.transitions:]
)
turing.turingMachineInfo()
tape.tapeInfo()

transitions = []
listOfStates = []
listOfStatesToExecute = []

for val in turing.transitions:
    transitions.append(val.split())

for t in transitions:
    state = State(
        t[StateConfig.atState],
        t[StateConfig.toState],
        t[StateConfig.read],
        t[StateConfig.write],
        t[StateConfig.move]
    )
    listOfStates.append(state)
    #state.stateInfo()

listOfStatesToExecute.append(turing.startState)

while listOfStatesToExecute:
    #print(listOfStatesToExecute)
    for listExecute in listOfStatesToExecute:
        print('Lista de Execução: ',listOfStatesToExecute)
        print('Estado de execução:', listExecute, '\n')
        tape.tapeInfo()

        for statesList in listOfStates:
            #print(statesList.state)
            if listExecute == statesList.state and tape.headData == statesList.read:
                statesList.stateInfo()
                #print('Conteudo HeadFita: ',tape.headData)
                tape.data[tape.head] = statesList.write
                tape.headMove(statesList.move)
                listOfStatesToExecute.append(statesList.toState)
                #tape.tapeInfo()
                if statesList.state == turing.endStates:
                    print('OK!')
                    #break


            #else:
            #    print('Estado de execução:', listExecute)
            #    print('Conteudo Fita: ',tape.headData)
            #    statesList.stateInfo()
            #    print('pass')

        print('Remove: ',listExecute,'\n\n')
        listOfStatesToExecute.remove(listExecute)
        break

        #print(listOfStatesToExecute)
print('OK!')
