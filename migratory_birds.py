def migratoryBirds(arr):
    bird = {}
    for n in arr:
        if n not in bird.keys():
            bird[n] = 1
        else:
            bird[n] += 1

    max, k = None, None
    for key, value in bird.items():
        if max is None:
            max, k = value, key
        elif max == value:
            max = value
        elif max < value:
            max = value
            k = key
    return k

array = list()
with open('input04.txt') as f:
    for line in f:
        tokens = line.split()
        for token in tokens:
            array.append(token)

print(migratoryBirds(array))
