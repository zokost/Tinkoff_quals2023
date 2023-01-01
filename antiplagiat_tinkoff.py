import argparse


def lev_distance(line1, line2):
    n, m = len(line1), len(line2)
    if n > m:
        line1, line2 = line2, line1
        n, m = m, n
    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if line1[j - 1] != line2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)
    return current_row[n]


def compare(line1, line2):
    length = max(len(line1), len(line2))
    return (1 - lev_distance(line1, line2) / length) * 100


parser = argparse.ArgumentParser()
parser.add_argument('file1')
parser.add_argument('file2')
args = parser.parse_args()
with open(args.file1, 'r') as f:
    lines = f.readlines()
documents = []
answers = []
for line in lines:
    line_words = line.split()
    documents += line_words
for i in range(1, len(documents), 2):
    print(documents[i])
    print(documents[i - 1])
    with open(documents[i], 'r') as f:
        text1 = f.read()
    with open(documents[i - 1], 'r') as f:
        text2 = f.read()
    with open(args.file2, 'a') as f:
        f.write(str(compare(text1, text2)))
        f.write('\n')
