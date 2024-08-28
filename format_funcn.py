'''
a = ['jac', 'vein', 'ryan']
b = ['tech', 'manage', 'production']

for i in range(0,len(a)):
    template = "{} is in {}"
    print(template.format(a[i],b[i]))
'''
str1 = "my name is {nm}, I am {age}"
print(str1.format(nm = "Nishant" , age = "18"))
