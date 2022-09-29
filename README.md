# Number of holes

A joke 'project' to demonstrate the use of neural networks to count the 'number of holes' in a number.

For example, 789 has 3 holes, 123 has none, 999888 and nine holes and so on. 4 is bit of a strange case; whether it has a hole or not depends on the font used. In this case... there's a hole in it.

data_gen.py is used to generate the dataset for the problem.

Model_creation.ipynb is self-explanatory.

utils.py contains helper functions which are used in the other files.

main.py generates a bunch of random numbers and uses the ANN model to predict the number of holes instead of using a rule-based system.
