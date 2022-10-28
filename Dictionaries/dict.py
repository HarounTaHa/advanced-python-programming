test_dict = {'k1': 'haroun', 'k2': 'taha'}
print(test_dict['k1'])
print(test_dict['k2'])

nested_dict = {'k1': {'j1': 'Test', 'j2': 'Test2'}, 'k2': {'c1': 'Test3', 'c2': 'Test4'}}
print(nested_dict['k1']['j1'])
print(nested_dict['k2']['c1'])

temp = nested_dict['k2']

print(temp)
print(temp['c2'])
