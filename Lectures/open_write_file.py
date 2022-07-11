fh = open('test.txt', 'w')
text = 'Serhii Korobchenko'
symbols_written = fh.write(text)
print(symbols_written)  # 6
fh.close()