d=dict.fromkeys(("name","age","some"),"unknown")
print(d)
a=dict.fromkeys(range(1,11),"siri")
print(a)
name={"son":"man","don":"sunil"}
print(name.get("son"))
if name.get("sons"):
          print("present")
else:
          print("not present")
# print(name.clear())
# print(name)
name1=name.copy()
print(name1)
print(name)