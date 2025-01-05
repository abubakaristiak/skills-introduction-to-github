class MySelf:
    def __init__(self, name, age, skills):
        self.name = name
        self.age = age
        self.skills = skills

    def introduce(self):
        print(f"Hello! My name is {self.name}.")
        print(f"I am {self.age} years old.")
        print("I have experience with the following programming languages:")
        for skill in self.skills:
            print(f"- {skill}")

my_profile = MySelf("Your Name", 25, ["Python", "JavaScript", "C++"])
my_profile.introduce()
