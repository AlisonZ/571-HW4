#Goals
Through this assignment you will:

* Explore dependency grammars and dependency parsing.
* Investigate transition-based parsing approaches in dependency parsing.
* Gain familiarity with representations of dependency parses.
* Implement the arc-standard oracle to identify and apply the correct transition sequence associated with a gold-standard dependency parse.

#Background
Please review the class slides, homework slides, and readings in the textbook on dependency parsing in general and transition-based parsing in particular. 

Transition-based dependency parsing relies on a transition set which converts the current state of the parse - referred to as a "configuration" - into a new state, until some terminal state is reached.  The arc-standard paradigm employs three transitions:

* SHIFT
* (LEFTARC,<label>)
* (RIGHTARC,<label>)
where <label> is the dependency relation that holds between the head and dependent identified by the transition.

The configuration consists of the stack, buffer, and arcs as discussed in class and in the readings.  It may be most straightforward to represent these as lists of different types, as in [0 1], [2,3,4],[] for a stack with two elements (including ROOT), a buffer with three elements, and (here) an empty set of arcs.  The elements here refer to the words in the sentence by their indexes.  Of course, alternate data structures are possible as well.

You will need to implement a function that applies a specified transition to a given configuration, and have code which implements the oracle which determines which transition should be applied to the current configuration, while working through each sentence with its accompanying dependency parse.

#Oracle 
Create a program to implement the arc-standard oracle and apply it to a set of dependency-parsed sentences. Specifically, your program should:

* Read in a set of dependency parses of sentences, in a simplified CONLL format.
* For each dependency parse, your program should output:
to one file, the ordered sequence of transitions corresponding to the parse
to another file, the dependency arcs corresponding to the application of the above transitions to the sentence.
Note: You are only responsible for implementing the oracle.  You do not need to train a model based on the oracle transitions.

# Programming
Create a program called hw4_oracle.sh which applies the arc-standard oracle to identify and apply the correct sequence of transitions from the dependency parses provided  invoked as:
hw4_oracle.sh <input_dependency_parse_filename> <output_dependency_filename> <output_sequence_filename> where,

* <input_dependency_parse_filename> is the name of the file holding the gold-standard dependency parses which you will use to derive the transition sequence.
* <output_dependency_filename> is the name of the file to write the resulting dependency arcs created by applying the oracle transitions.
* <output_sequence_filename> is the name of the file to write the resulting sequence of transitions derived by the arc-standard oracle, which could be used in training a full dependency parser.
# Files
Example and Test Data Files
All data and example files may be found on Patas in /dropbox/25-26/571W/hw4.

* conll.simple: Set of English dependency parses from the CONLL 2007 shared task, in a simplified four column format,
<index>\t<word>\t<depenendency_relation>\t<head_index>
ROOT corresponds to head_index 0
Blank lines separate parses
* toy.dep: Toy set of dependency parses.
* toy.seq: Oracle sequence of transitions corresponding to the dependency parses in toy.dep. This is just an example file to illustrate the desired format.

# Submission Files
* hw.tar.gz: Tarball containing:
hw4_oracle.sh: Primary program file with language-appropriate extension.
Python script(s) invoked by your shell script.
* hw4_dependencies_output.txt: This file should contain the dependency arcs resulting from applying the oracle transitions to conll.simple. They should be in the simplified CONLL format described above, and sorted by word index.  Correct output should replicate the original dependency parse.
* hw4_transitions_output.txt: The output file with the sequence of transitions derived from the original dependency parses, using the arc-standard transition inventory, given above.
* readme.{txt|pdf}: Write-up file
This file should describe and discuss your work on this assignment. Include problems you came across and how (or if) you were able to solve them, any insights, special features, and what you learned. Give examples if possible. If you were not able to complete parts of the project, discuss what you tried and/or what did not work. This will allow you to receive maximum credit for partial work.
