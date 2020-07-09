s=str(input("Enter file name with extension:"))
spos=s.find('.')
epos=s.find(' ',spos)
ext=s[spos+1::]
print(ext)
if ext== 'py':
    print("python")
else:
    print("Not a python file")
