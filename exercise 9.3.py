class User():
    """docstring for User."""
    def __init__(self, f_name, l_name, gender, age, joined):
        self.firstname = f_name
        self.lastname = l_name
        self.age = age
        self.gender = gender
        self.joined = joined

    def describe_user(self):
        print("\nContact Details")
        print('Name: ' + self.firstname + " " + self.lastname)
        print("Age: " + self.age)
        print("Gender: " + self.gender)
        print("Joined: " + self.joined)

    def greet_user(self):
        print("\nHello " + self.firstname + "!")

obj = User("dani","david","Male","21","25 feb 2018")
obj.describe_user()
obj.greet_user()
        