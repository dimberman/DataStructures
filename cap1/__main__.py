from binary_tree import *
from linked_list import *
from datastructure_analyzer import *
from hash_table_chaining import *
from hash_table import *
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--data-structure', default=0,
                    help='which data structure to use\n'
                         '1: BST\n'
                         '2: Hastable\n'
                         '3: Hashtable with chaining\n'
                         '4: LinkedList')
parser.add_argument('--worst-case', default=False, help='whether to specifically test the worst-possible case for DS')


def to_csv_line(otype, ftype, atype, input):
    a = [otype, ftype,atype]
    a.extend(input)
    return ',\t'.join(str(e) for e in a)


def print_list(otype, ftype, ans):
    min_val = [l[0] for l in ans]
    avg_val = [l[1] for l in ans]
    max_val = [l[2] for l in ans]

    print to_csv_line(otype, ftype, 'min', min_val)
    print to_csv_line(otype, ftype, 'avg', avg_val)
    print to_csv_line(otype, ftype, 'max', max_val)


def find_ds(ds_input):
    if ds_input == 1:
        ds_tmp = BSTStepCounter()
    elif ds_input == 2:
        ds_tmp = HashTable()
    elif ds_input == 3:
        ds_tmp = HashTableChainingStepCounter(1)
    elif ds_input == 4:
        ds_tmp = LinkedListStepCounter()
    else:
        raise Exception('invalid input')
    return ds_tmp


args = parser.parse_args()
ds_num = args.data_structure

path = 'cap1/data.txt'

f = open(path, 'r')
lines = []
for x in range(900):
    lines.append(f.readline())

i = 100
res_list = []
while i <= 800:
    ds = find_ds(int(ds_num))
    curr_lines = lines[:i]
    b = BigOAnalyzer(ds)
    res_list.append(b.test_insert(curr_lines))
    i *= 2
    f.close()

print_list(type(ds).__name__, 'insert', res_list)

i = 100
res_list = []


while i <= 800:
    ds = find_ds(int(ds_num))
    curr_lines = lines[:i]
    for x in lines:
        ds.insert(x)
    b = BigOAnalyzer(ds)
    res_list.append(b.test_lookup(curr_lines))
    i *= 2

print_list(type(ds).__name__, 'lookup', res_list)
i = 100
res_list = []

while i <= 800:
    ds = find_ds(int(ds_num))
    curr_lines = lines[:i]
    for x in curr_lines:
        ds.insert(x)
    b = BigOAnalyzer(ds)
    curr_lines = list(reversed(curr_lines))
    res_list.append(b.test_lookup(curr_lines))
    i *= 2
print_list(type(ds).__name__, 'delete', res_list)
