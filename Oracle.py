class Oracle:
    def __init__(self):
        self.buffer = []
        self.stack = []
        self.transitions = []
        self.input_phrase = ''

    def set_buffer(self, buffer_input):
        self.buffer = buffer_input

    def set_input_phrase(self, phrase):
        self.input_phrase = phrase
    
    def get_buffer(self):
        return self.buffer
    
    def get_input_phrase(self):
        return self.input_phrase
    
    def get_stack(self):
        return self.stack
    
    def get_transitions(self):
        return self.transitions
    
    def is_terminal_case(self):
        buffer_len = len(self.buffer)
        stack_len = len(self.stack)
        transition_len = len(self.transitions)
        
        if buffer_len == 0 and stack_len == 1 and transition_len != 0:
            return True
        else:
            return False
    
    def add_transition(self, transition):
        self.transitions.append(transition)

    def add_to_stack(self, token):
        self.stack.append(token)
    
    def shift(self):
        shifted_el = self.buffer.pop(0)
        self.stack.append(shifted_el)

    def view_top_two(self):
        right = self.stack.pop()
        left = self.stack.pop()
        return right, left
    
    def print_buffer(self):
        print(f"BUFFFFFF: {self.buffer}")

    def print_stack(self):
        print(f"STACK!!!! {self.stack}")
   
