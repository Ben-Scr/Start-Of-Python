from os import read
import classes
import polymorphism
from methods import Math
from methods import Random
from methods import File

# IO-Stream
File.writeAllText("Test.txt", "This is a test");
print(File.readAllText("Test.txt"))

# OOP
p1 = classes.Person("Max", 20);
p1.present();

# Input output
uInput = input();
print(uInput)

# Methods
print(Math.add(1, 2));
print(Math.clamp(0, 1, 6));

# "Polymorthism"
polymorphism.printType(p1);

# Lists
numbers = [1, 2, 3, 4]
numbers.append(5);
print("Numbers: " + numbers);

print("Random between (0, 1000): " + Random.next(0, 1000));
