f = open('first_test_file.csv',encoding="latin-1")
f.readline() # ignore first line because of wrong format
lst = f.readlines()

summa = 0
for line in lst:
    line = line.strip()
    data = line.split(',')
    # print(line_lst)
    time, num = data[:2]
    # print(time, num)
    summa += float(num)
f.close()

print(summa)
