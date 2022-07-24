class Person:
    def __int__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫 %s 体重是 %.2f 公斤" % (self.name, self.weight)

    def run(self):
        pass

    def eat(self):
        pass

xiaoming = Person("小明" , 75.0)

xiaoming.run()
xiaoming.eat()

print(xiaoming)
