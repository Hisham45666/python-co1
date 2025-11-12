my_dict = {'b': 3, 'a': 1, 'c': 2}

ase = dict(sorted(my_dict.items()))
print("ascending order:" ,ase)

desc = dict(sorted(my_dict.items(), reverse=True))
print("descending order:" ,desc)
