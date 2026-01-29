
import sys
import os
from Oracle import Oracle
from Token import Token
TRANSITIONS = {
    'shift': "SHIFT",
    'leftArc': "LEFTARC",
    'rightArc': "RIGHTARC"
}

def get_inputs():
    if len(sys.argv) > 1:
        parse_input = sys.argv[1]
        dependency_output = sys.argv[2]
        sequence_output = sys.argv[3]

    if os.path.exists(dependency_output):
        os.remove(dependency_output)

    if os.path.exists(sequence_output):
        os.remove(sequence_output)
    
    return parse_input, dependency_output, sequence_output

def get_transition(right_token, left_token):
    r_head = right_token.get_head_index()
    r_index = right_token.get_index()
    r_pos = right_token.get_pos()
    l_head = left_token.get_head_index()
    l_index = left_token.get_index()
    l_pos = left_token.get_pos()
    
    if r_head == l_index:
        return (TRANSITIONS['rightArc'], r_pos)
    elif l_head == r_index:
        return (TRANSITIONS['leftArc'], l_pos)
    else: 
        return (TRANSITIONS['shift'])

def print_sequence(o, sequence_output):
    transitions = o.get_transitions()
    with open(sequence_output, "a") as f:
        for transition in transitions:
            print(transition, file=f)
        print('', file=f)

def create_transitions(o, sequence_output):
    is_terminal_case = o.is_terminal_case()
    if is_terminal_case:
        o.add_transition((TRANSITIONS['rightArc'], 'ROOT'))
        print_sequence(o, sequence_output)
        return 
    while not is_terminal_case:
        stack = o.get_stack()
        if len(stack) > 1:
            right, left = o.view_top_two()            
            transition = get_transition(right_token=right, left_token=left)
            o.add_transition(transition)

            if transition[0] == TRANSITIONS['rightArc']:
                o.add_to_stack(left)
            if transition[0] == TRANSITIONS['leftArc']:
                o.add_to_stack(right)
            if transition == TRANSITIONS['shift']:
                o.add_to_stack(left)
                o.add_to_stack(right)
                o.shift()
        else:
            is_terminal_case = o.is_terminal_case()
            if is_terminal_case:
                o.add_transition((TRANSITIONS['rightArc'], 'ROOT'))
                print_sequence(o, sequence_output)
                return
            else:
                o.shift()
                o.add_transition(transition=TRANSITIONS['shift'])
    

def create_oracle(parsed_phrase, sequence_output):
    o = Oracle()
    tokens = []
    for token in parsed_phrase:
        t = Token()
        t.create_token(token.strip())
        tokens.append(t)
    
    root_token = tokens.pop(0)
    o.add_to_stack(root_token)
    o.set_buffer(tokens)
    o.add_transition(transition=TRANSITIONS['shift'])
    create_transitions(o, sequence_output)

def read_dependency_parses(parse_input, sequence_output):
    with open(parse_input, 'r', encoding='utf8') as file:
        lines = file.readlines()
        parsed_phrase = []
        for line in lines:
            if line == "\n":
                create_oracle(parsed_phrase, sequence_output)
                parsed_phrase = []
            else:
                parsed_phrase.append(line)
        
        create_oracle(parsed_phrase, sequence_output)
      

def main():
    parse_input, dependency_output, sequence_output = get_inputs()
    read_dependency_parses(parse_input, sequence_output)

if __name__ == '__main__':
    main()