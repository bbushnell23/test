import os

input_file = '/etc/passwd'
output_file = '/docs/test1.txt'

os.makedirs(os.path.dirname(output_file), exist_ok=True)

with open(input_file, 'r') as infile:
    contents = infile.read()

with open(output_file, 'w') as outfile:
    outfile.write(contents)
