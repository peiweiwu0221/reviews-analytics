data = []
count = 0
sum_len = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
for d in data:
    sum_len = sum_len + len(d)
average=sum_len/count
print('留言的平均長度',average)