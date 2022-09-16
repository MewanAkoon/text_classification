import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--augmented_input', help='input data file')
parser.add_argument('--output', help='train/test output file')
parser.add_argument('--label_output', help='train/test output label file')

args = parser.parse_args()

with open(args.output, 'w') as file1:
  with open(args.label_output, 'w') as file2:
    with open(args.augmented_input,'r') as file:
      for line in file:
        data = line.strip().split('\t')
        train_labels = data[0]
        train = data[1]
        print(train, file=file1)
        print(train_labels, file=file2)

print('Splitted file', args.augmented_input)        