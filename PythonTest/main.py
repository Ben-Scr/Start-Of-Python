import classes
import polymorphism
from methods import Math

# OOP
p1 = classes.Person("Max", 20);
p1.present();

# Methods
print(Math.add(1, 2));
print(Math.clamp(0, 1, 6));

# "Polymorthism"
polymorphism.printType(p1);

# Lists
numbers = [1, 2, 3, 4]
numbers.append(5);
print(numbers);
