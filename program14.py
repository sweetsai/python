class person:
    count=0
    def __init__(self,name,age,collegename):
        self.name=name
        self.age=age
        self.collegename=collegename
        person.count+=1
person1=person("sai",20,"AWEC")
person2=person("sudha",20,"AWEC")
print(person.count)
print(person1.name)
print(person2.age)
print(person1.collegename)
