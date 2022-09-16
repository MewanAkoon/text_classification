import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--input_1', help='train/test file')
parser.add_argument('--input_2', help='train/test label file')
parser.add_argument('--output', help='output data file')

args = parser.parse_args()

with open(args.output, 'w') as file3:
  with open(args.input_2, 'r') as file1:
    with open(args.input_1, 'r') as file2:
      for line1, line2 in zip(file1, file2):
        print(line1.strip(), '\t', line2.strip(), file=file3)

print('Created file', args.output)