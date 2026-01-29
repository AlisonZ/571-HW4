class Oracle:
    def __init__(self):
        self.buffer = []
        self.stack = []
        self.transitions = {}

    def set_buffer(self, buffer_input):
        self.buffer = buffer_input

    def add_transition(self, transition):
        print(f"TRANSITION ADDDDD")
    
    def shift(self):
        shifted_el = self.buffer.pop()
        self.stack.append(shifted_el)
    
    def left_arc(self):
        print(f"LEFT")

    def right_arc(self):
        print(f"RIGHT")

    def view_top_two(self):
        print("TOP 2")
    

    def print_buffer(self):
        print(f"BUFFFFFF: {self.buffer}")
    
   
