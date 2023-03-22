#collections

from collections import Counter

a_list = [1, 1, 1, 1, 4, 6, 79, 79, 80, 4, 4, 4, 4]
col1 = Counter(a_list)
print(col1.keys())