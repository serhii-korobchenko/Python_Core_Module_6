fh = open('test.txt', 'w+')
fh.write('hello!')

position = fh.tell()
print(position) # 6

fh.seek(1)
position = fh.tell()
print(position) # 1

fh.read(2)
position = fh.tell()
print(position) # 3

fh.close()