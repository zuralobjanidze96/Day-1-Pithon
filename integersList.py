def integersList(list):
    s = list[0]
    for i in range(len(list)):
        if s >= list[i]:
            continue
        else:
            s = list[i]
    return s

x = integersList([0, 1, 2, 3, 4, 4])

print(x)