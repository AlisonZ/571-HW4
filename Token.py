class Token:
    def __init__(self):
        self.index = 0
        self.head_index = 0
        self.word = ''
        self.pos = ''

    def set_index(self, i):
        self.index = i 
    
    def set_head_index(self, i):
        self.head_index = i
    
    def set_word(self, word):
        self.word = word
    
    def set_pos(self, pos):
        self.pos = pos
        
    def create_token(self, token):
        split_token = token.split("\t")
        index = split_token[0]
        word = split_token[1]
        pos = split_token[2]
        head_i = split_token[3]

        self.set_index(index)
        self.set_word(word)
        self.set_pos(pos)
        self.set_head_index(head_i)

    def print_token(self):
        print("**************")
        print(f"INDEX {self.index}")
        print(f"HEAD {self.head_index}")
        print(f"WORD {self.word}")
        print(F"POS {self.pos}")
