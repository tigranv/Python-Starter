
string = 'First Line of text. ' \
    'Second line of text'

print(string)

print('----------------------')

string = 'First Line of text. \
          Second line of text'

print(string)

print('----------------------')

string = 'First Line of text. \n' \
          'Second line of text'

print(string)

print('----------------------')

multiline_string = ''' lesson2 bla bla bla
-int
-bool
-float
-complex
-string'''

print(multiline_string)

print('----------------------')

s = "hello"
print(s[0] + s[3])

print('----------------------')

s = 'Number = %d' % 17
print(s)
# %f, %s
print('----------------------')

s = "number = {}".format(17)
print(s)

s = "number {0} = {1}".format("hello", 456)
print(s)
