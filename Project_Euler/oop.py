class Person(object):
    def __init__(self, name):
        self.name = name
    def reveal(self):
        print(f"My name is {self.name}")

class Hero(Person):
    def __init__(self, name, hero_name):
        super().__init__(name)
        self.hero_name = hero_name
    def reveal(self):
        super().reveal()
        print(f"And I am {self.hero_name}")




jacob = Person("Jacob")
jacob.reveal()

bruce = Hero("Bruce", "Batman")
bruce.reveal()