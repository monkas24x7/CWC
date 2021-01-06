import re
s1=input()
s2=input()
print(re.subn(f"[{s2}]","",s1,flags=re.IGNORECASE)[0])

