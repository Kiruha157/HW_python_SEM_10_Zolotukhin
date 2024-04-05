import random
import pandas as pd

def one_hot_human(type) -> int:
    return 1 if type == 'human' else 0

def one_hot_robot(type) -> int:
    return 1 if type == 'robot' else 0


lst = ['robot'] * 10
#print(lst)
lst += ['human'] * 10
#print(lst)
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

data['human'] = [one_hot_human(i) for i in data['whoAmI']]
data['robot'] = [one_hot_robot(i) for i in data['whoAmI']]

del data['whoAmI']

print(data.head())

#test = pd.get_dummies(data['whoAmI'])

