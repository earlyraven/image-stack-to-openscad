To view options and syntax to use, run in command line:
python main.py -h

To generate examples, run in command line:
bash example_generator.sh

To generate examples and update showcase, run in command line:
bash pre_push.sh

To save terminal output to a file:
python main.py OPTIONS_AND_FILES > output.txt

example usage: (assuming files are in current working directory):
python main.py --with cr3.txt cr2.txt cr1.txt > thethree.scad
python main.py --with cr3.txt cr2.txt cr1.txt --vs 20 > thethree_given_cubesize.scad
