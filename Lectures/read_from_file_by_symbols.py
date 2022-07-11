fh = open('test.txt', 'w')
fh.write('hello!')
fh.close()

fh = open('test.txt', 'r')
while True:
    symbol = fh.read(1) #--> 1 - number of bites - optional parameter
    if len(symbol) == 0:
        break
    print(symbol)

fh.close()