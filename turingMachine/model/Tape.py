class Tape:
    def __init__(self, data, head, headData):
        self.data = data
        self.head = head
        self.headData = headData


    def tapeInfo(self):
        print('Conteudo da Fita: ',self.data)
        print('Posição Head: ',self.head)
        print('Conteudo Head: ',self.headData, '\n')


    def headMove(self, string):
        if not(string == 'L' and self.head == 0):
            if(string == 'R'):
                self.head += 1
                self.headData = self.data[self.head]
            if(string == 'L'):
                self.head -= 1
                self.headData = self.data[self.head]
