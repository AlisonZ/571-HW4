
import sys
import os
from Oracle import Oracle
from Token import Token
from ArcModel import Arc
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

def create_transitions(o, sequence_output, dependency_output):
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

            if transition[0] == TRANSITIONS['rightArc']:
                o.add_transition(transition)
                o.add_to_stack(left)
            if transition[0] == TRANSITIONS['leftArc']:
                o.add_transition(transition)
                o.add_to_stack(right)
            if transition == TRANSITIONS['shift']:
                if len(o.get_buffer()) > 0:
                    o.add_to_stack(left)
                    o.add_to_stack(right)
                    o.add_transition(transition)
                    o.shift()
                else:
                    break
            is_terminal_case = o.is_terminal_case()
        else:
            is_terminal_case = o.is_terminal_case()
            if is_terminal_case:
                o.add_transition((TRANSITIONS['rightArc'], 'ROOT'))
                print_sequence(o, sequence_output)
                create_dependency_arcs(o, dependency_output)
                return
            else:
                o.shift()
                o.add_transition(transition=TRANSITIONS['shift'])

    print_sequence(o, sequence_output)
    create_dependency_arcs(o, dependency_output)

def print_dependency_arcs(arcs, dependency_output):
    sorted_arcs = sorted(arcs, key=lambda arc: int(arc.get_index()))
    with open(dependency_output, "a") as output_file:
        for arc in sorted_arcs:
            i = arc.get_index()
            head = arc.get_head_index()
            word = arc.get_word()
            pos = arc.get_dep_relation()

            print(f"{i} {word} {pos} {head}", file=output_file)
        print('\n', file=output_file)

def create_dependency_arcs(o, dependency_output):
    phrase = o.get_input_phrase()
    sequence = o.get_transitions()
    stack = []  
    root_token = "0\tROOT\tROOT\t0"                                                      
    stack.append(root_token)                                                                                   

    arcs = []

    for seq in sequence:
        s = ''
        if len(seq[0]) == 1:
            s = seq
        else:
            s = seq[0]
        
        if s == TRANSITIONS['shift']:
            popped = phrase.pop(0)
            stack.append(popped)
        elif s == TRANSITIONS['leftArc']:
            right = stack.pop()
            left = stack.pop()
            left_split  = left.split('\t')
            right_split = right.split('\t')

            a = Arc()
            a.set_head_index(right_split[0])
            a.set_index(left_split[0])
            a.set_word(left_split[1])
            a.set_dep_relation(left_split[2])

            arcs.append(a)
            stack.append(right)
       
        elif s == TRANSITIONS['rightArc']:
           right = stack.pop()
           left = stack[-1]
           right_split = right.split('\t')
           left_split = left.split('\t')

           a = Arc()
           a.set_head_index(left_split[0])
           a.set_index(right_split[0])
           a.set_word(right_split[1])
           a.set_dep_relation(right_split[2])
           arcs.append(a)

    print_dependency_arcs(arcs, dependency_output)

def create_oracle(parsed_phrase, sequence_output, dependency_output):
    o = Oracle()
    o.set_input_phrase(phrase=parsed_phrase)
    tokens = []
   
    for token in parsed_phrase:
        t = Token()
        t.create_token(token.strip())
        tokens.append(t)
    
    if not tokens:
        return
    
    root_token = tokens.pop(0)
    o.add_to_stack(root_token)
    o.set_buffer(tokens)
    o.add_transition(transition=TRANSITIONS['shift'])
    create_transitions(o, sequence_output, dependency_output)

def read_dependency_parses(parse_input, sequence_output, dependency_output):
    with open(parse_input, 'r', encoding='utf8') as file:
        lines = file.readlines()
        parsed_phrase = []
        for line in lines:
            if line == "\n":
                if parsed_phrase:
                    create_oracle(parsed_phrase, sequence_output, dependency_output)
                parsed_phrase = []
            else:
                parsed_phrase.append(line)
        
        create_oracle(parsed_phrase, sequence_output, dependency_output)
      

def main():
    parse_input, dependency_output, sequence_output = get_inputs()
    read_dependency_parses(parse_input, sequence_output, dependency_output)

if __name__ == '__main__':
    main()