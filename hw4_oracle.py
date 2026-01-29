
import sys
import os
from Oracle import Oracle
from Token import Token

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

def create_oracle(parsed_phrase):
    o = Oracle()
    tokens = []
    for token in parsed_phrase:
        t = Token()
        t.create_token(token.strip())
        tokens.append(t)

    o.set_buffer(tokens)
    o.print_buffer()

def read_dependency_parses(parse_input):
    with open(parse_input, 'r', encoding='utf8') as file:
        lines = file.readlines()
        parsed_phrase = []
        for line in lines:
            if line == "\n":
                create_oracle(parsed_phrase)
                parsed_phrase = []
            else:
                parsed_phrase.append(line)
        
        create_oracle(parsed_phrase)

def main():
    parse_input, dependency_output, sequence_output = get_inputs()
    read_dependency_parses(parse_input)

if __name__ == '__main__':
    main()