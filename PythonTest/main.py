import classes
import polymorphism
from methods import Math

p1 = classes.Person("Max", 20);
p1.present();
print(Math.add(1, 2));
print(Math.clamp(0,1, 6));
polymorphism.printType(p1);