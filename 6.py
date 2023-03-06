bad_chars = [';', ':', '!', "*", " " , "#"]
str1= "Ge;ek * s:fo ! r;Ge * e*k:s !"
str2= "Jo;ko:okiwj #ple!"
str3= "k;sk:in*seaso#n"
print("Original String : " + str1)
print("Original String : " + str2)
print("Original String : " + str3)
for i in bad_chars:
     str1 = str1.replace(i, '')
     str2 = ''.join(i for i in str2 if not i in bad_chars)
     str3 = ''.join((filter(lambda i: i not in bad_chars,str3)))
print("Result is : " + str(str1))
print("Result is : " + str(str2))
print("Result is : " + str(str3))

