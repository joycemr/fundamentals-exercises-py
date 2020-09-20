def find_odd_int(odd_int):
    intDict = {}
    for num in odd_int:
        x = intDict.get(num)
        if x:
            intDict.update({num: x + 1})
        else:
            intDict.update({num: 1})
    for key, val in intDict.items():
        # print('key is: {}, val is: {}, val % 2 is: {}'.format(key, val, val % 2))
        if val == 1 or not val % 2 == 0:
            print('answer: {}'.format(key))

find_odd_int([1,2,3,1,2,3,1,2,3,1,2,3,1])
