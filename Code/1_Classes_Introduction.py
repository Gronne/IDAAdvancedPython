

from dataclasses import dataclass


def print_full_name_of_oldest_person(p_f_1: str, p_l_1: str, p_a_1: str, p_f_2: str, p_l_2: str, p_a_2: str):
    if p_a_1 > p_a_2:
        print(f"{p_f_1} {p_l_1}")
    else:
        print(f"{p_f_2} {p_l_2}")


person_1_first_name: str = "Mathias"
person_1_last_name: str = "Grønne"
person_1_age: int = 29

person_2_first_name: str = "Tobias"
person_2_last_name: str = "Nielsen"
person_2_age: str = 35

print_full_name_of_oldest_person(
    person_1_first_name,
    person_1_last_name,
    person_1_age,
    person_2_first_name,
    person_2_last_name,
    person_2_age
)





class Person:

    def __init__(self, first_name: str, last_name: str, age: int = 25):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self._balance: float = 0.0


    @property
    def full_name(self) -> str:
        '''
        Get the person's full name
        '''
        return f"{self.first_name} {self.last_name}"


    @property
    def balance(self) -> float:
        '''
        Get how much money the person got in the bank
        '''
        return self._balance


    def spend_money(self, amount: float) -> None:
        '''
        The person used this amount of money
        '''
        if amount > 0:
            self._balance -= amount

    
    @property
    def is_adult(self) -> bool:
        '''
        Check if the person is an adult
        '''
        return self.age > 0
    

    @property
    def info_as_string(self) -> str:
        '''
        Get info as a string
        '''
        string: str = f"Person\n"
        string += f"  Name: {self.full_name}\n"
        string += f"  Age: {self.age}\n"
        string += f"  Balance: {self.balance}\n"
        return string





person_1 = Person(
    "Mathias",
    "Grønne",
    29
)

person_2 = Person(
    first_name="Tobias",
    last_name="Nielsen",
    age=35
)


print(person_1.first_name)
print(person_2.age)

print(person_1.full_name)
print(person_1.balance)

person_1.last_name = "Pedersen"
print(person_1.full_name)


def print_full_name_of_oldest_person(person_a: Person, person_b: Person) -> None:
    oldest_person: Person = person_b if person_a.age < person_b.age else person_b
    print(f"Oldest Person: {oldest_person.full_name}")

print_full_name_of_oldest_person(person_1, person_2)


#player_1.balance = 100000
#print(player_1.balance)

print(person_1.info_as_string)

person_1.spend_money(49)
print(person_1.info_as_string)

person_1.spend_money(-100000)
print(person_1.info_as_string)




@dataclass
class Pet:
    name: str
    age: int
    owner: Person

    @property
    def family_pet_name(self) -> str:
        return f"{self.name} {self.owner.last_name}"


person = Pet(name="Felix", age=29, owner=person_1)
print(person)
print(person.family_pet_name)



