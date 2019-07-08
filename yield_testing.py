def load_fine():
    with open('single_seg.txt','r',encoding='utf-8') as file:
        for line in file:
            line = line.strip('\n')
            line = line.split(' ')
            yield line


g = load_fine()
index = 0
for i in range(1000):
    try:
        print(next(g))
        index +=1
    except StopIteration:
        # g.close()
        g = load_fine()

print(index)