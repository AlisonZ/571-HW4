
import sys
import os

def get_inputs():
    if len(sys.argv) > 1:
        parse_input = sys.argv[1]
        dependency_output = sys.argv[2]
        sequence_output = sys.argv[3]

    if os.path.exists(dependency_output):
        os.remobve(dependency_output)

    if os.path.exists(sequence_output):
        os.remove(sequence_output)
    
    return parse_input, dependency_output, sequence_output

def main():
    parse_input, dependency_output, sequence_output = get_inputs()
    print("hiiii")

if __name__ == '__main__':
    main()