data = []
count = 0
new = []
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
    for d in data:
        if len(d) < 100:
            new.append(d)

print('一共有',len(new), '比留言長度小於100')
print(new[0])

good =[]
for d in data:
    if 'good' in d:    #good有沒有在裡面
        good .append(d) 

print('一共有',len(good), 'good有在裡面')
print(good[0])

