def prepend(elem, lt = []):
    #lt = lt if lt else[]
    lt.insert(0, elem)
    print (lt)
    #lt.append(elem)
    return lt
count = 0;
#print(prepend(1110),"---", prepend(40,[10,20]),"----",prepend(30),"---")
def filter_lt(predicate,lt):
    result = []
    for elem in lt:
        if(predicate(elem)):
            result.append(elem)
    return result
def element6(elem):
    return len(elem) > 6
lt = ['Justin', 'Anoymouns']
print(filter_lt(element6, lt))

