def add_commas(x):
    s = str(x)
    li = []
    for i in range(-len(s) // 3 * 3, -3, 3):
        li = li + [s[i:i+3]]
    li = li + [s[-3:]]
    return ','.join(li)

out = open('output.txt', 'w')
print(add_commas(2 ** 69420), file=out)
out.close()
