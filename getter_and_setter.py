#getter => get
#setter => set


class Adult:
    def __init__(self, age):
        self.age = age
        
    @property  # method to make a getter for age
    def age(self):
            """Getter for age"""
            print("Get age...")
            return self._age

    @age.setter # setter method => check for new value
    def age(self, new_age):
        if new_age < 18:
            print(f"{new_age} could not be entered. Age should be 18 or above for adults")
        else:
            self._age = new_age
        

#create a new person:
person1 = Adult(24)

print(person1.age)

#set new age and check
person1.age = 10

 
    
    