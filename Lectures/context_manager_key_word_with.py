fh = open('text.txt')
try:
    def some_useful_function(fh):
        pass
finally:
    fh.close()

#  The same result
#        ^
#        |
with open('text.txt', 'w+') as fh:
    def some_useful_function(fh):
        pass