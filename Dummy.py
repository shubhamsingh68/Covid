pers = [
    {
        'name': 'a',
        'age': 20
    },
    {
        'name': 'b',
        'age': 22
    },
    {
        'name': 'p',
        'age': 18
    },
    {
        'name': 'd',
        'age': 19
    },
    ]
############ Approach 1 ##########
# def shubham(key1):
#     # print(key1)
#     return key1['age']
############ Approach 2 ##########
# shubham = lambda key1: key1['age']

############ Approach 3 using inline lamda function ##########
pers.sort(key=lambda key1: key1['age'], reverse=True)
print(pers)
for i in pers:
    print(i)

