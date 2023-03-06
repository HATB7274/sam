char1 = input('Enter a Lower Case Letter:')
char2 = input('Enter a Upper Case Letter:')
print('Letter\t ASCII Value')
print(char1,'\t',ord(char1))
print(char2,'\t',ord(char2))
print('Difference Between ASCII Value of two letters:')
print(ord(char1),'-',ord(char2),'=',end=' ')
print(ord(char1)-ord(char2))

