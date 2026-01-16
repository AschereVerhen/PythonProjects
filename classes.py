# First Class:
class Robot:
    def __init__(self, name, manufacture):
        self.name = name
        self.manufacture = manufacture
    def greet(self):
        print(f"Hello World! I am {self.name}, and my model is {self.manufacture}")

# Exercises:
"""

    Exercise 1: The "Smart Light" (Beginner)

    The Goal: Practice basic state management and methods. In Rust, you might use a struct Light { is_on: bool, brightness: u8 }.

    Task: Create a SmartLight class.

    Requirements:

        An __init__ method that sets is_on to False and brightness to 0 by default.

        A method turn_on() that sets is_on to True.

        A method set_brightness(level) that only sets the brightness if the light is actually on.

        A __str__ method so that when you print(light), it says "The light is [ON/OFF] at brightness [X]".

"""

class SmartLight:
    def __init__(self, max_val: int):
        self.is_on: bool = False
        self.brightness: int = 0
        self.max_val: int = max_val

    def turn_on(self) -> None:
        self.is_on = True
        self.brightness: int = self.max_val

    def get_max(self) -> int:
        return self.max_val

    def turn_off(self) -> None:
        self.is_on = False
        self.brightness = 0

    def set_brightness(self, level: int):
        if self.is_on:
            self.brightness = level

    def __str__(self) -> str:
        if self.max_val != 0:
            brightness_precent = int((self.brightness / self.max_val) * 100)
        else:
            brightness_precent = 0
        return f"The light is {"ON" if self.is_on else "OFF"} at brightness level {brightness_precent}%."

"""
    Exercise 2: The "Payment Processor" (Intermediate)

    The Goal: Practice Inheritance (Python's version of shared behavior). In Rust, you would use a Trait called Payable. In Python, we can use a "Base Class."

    Task: Create a system for different payment types.

    Requirements:

        Create a base class PaymentMethod. Give it a method process(amount) that simply raises a NotImplementedError (this is like a trait requirement).

        Create two subclasses: CreditCard and Crypto.

        CreditCard should take a card_number in its constructor.

        Crypto should take a wallet_address.

        Implement the process(amount) method in both subclasses to print a unique message (e.g., "Charging $X to card [Number]").
"""

from abc import ABC, abstractmethod
class PaymentMethod(ABC): #defining as the abstract base class
    @abstractmethod
    def process(self, amount: int):
        raise NotImplementedError

class CreditCard(PaymentMethod):
    def __init__(self, card_number: int):
        self.card_number: int = card_number
    def process(self, amount: int) -> None:
        print(f"Charging ${amount} to card {self.card_number}")

class Crypto:
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address
    def process(self, amount: int) -> None:
        print(f"Charging ${amount} to wallet {self.wallet_address}")



"""
    Exercise 3: The "Stack" with Magic Methods (Advanced)

    The Goal: Practice Dunder Methods and mimicking Rust-style safety. In Rust, you love the Vec and how it handles bounds. Let's make a custom Stack.

    Task: Create a class SecureStack that wraps a Python list.

    Requirements:

        Implement __len__ so you can call len(my_stack).

        Implement __add__ (Operator Overloading) so that stack1 + stack2 returns a new stack containing elements of both.

        Create a push method and a pop method.

        The Twist: In the pop method, if the stack is empty, don't just crash. Return None (mimicking Rust's Option<T>).
"""

#First implementing Option<T>
from typing import Generic, TypeVar, Optional, Iterable

T = TypeVar("T")

class Option(Generic[T]):
    def is_some(self) -> bool: raise NotImplementedError
    def is_none(self) -> bool: return not self.is_some() # They are opposites anyways
    def unwrap(self) -> T: raise NotImplementedError
    def unwrap_or(self, default: T) -> T: raise NotImplementedError
    def __str__(self) -> str: raise NotImplementedError

class Some(Option[T]):
    __slots__ = ("__value",)
    def __init__(self, value): self.__value = value
    def is_some(self) -> bool: return True
    def unwrap(self) -> T: return self.__value
    def unwrap_or(self, default: T) -> T: return self.__value
    def __str__(self) -> str:
        return f"Some({self.__value})"

class Nothing(Option[T]):
    def is_some(self) -> bool: return False
    def unwrap(self) -> T: raise RuntimeError("Called unwrap on a None value")
    def unwrap_or(self, default: T) -> T: return default
    def __str__(self) -> str:
        return "Nothing"

T = TypeVar("T")
class SecureStack(Generic[T]):
    def __init__(self, stack_val: Optional[Iterable[T]] = None):
        self.values: [T] = stack_val if stack_val is not None else []

    def __len__(self):
        return self.values.__len__()
    def __add__(self, other: SecureStack[T]) -> SecureStack[T]:
        return SecureStack(self.values + other.values)
    def push(self, element: T) -> None:
        self.values.append(element)
    def pop(self) -> Option[T]:
        if not self.values:
            return Nothing()
        return Some(self.values.pop())
    def __str__(self) -> str:
        return f"SecureStack({self.values})"

"""
CODE:
        securelist = SecureStack()
        securelist.push("Hello")
        securelist.push("World!")
        new_securelist = SecureStack(["What", "A", "Wonderfull", "Day", "Innit?"])
        securelist = securelist + new_securelist
        print(securelist.__len__())
        print(securelist.pop())
        print(securelist.pop())
        print(securelist.pop())
        print(securelist.pop())
        print(securelist.pop())
        print(securelist.pop())
        print(securelist.pop())
        print(securelist.pop())
"""

"""
OUTPUT:
        7
        Some(Innit?)
        Some(Day)
        Some(Wonderfull)
        Some(A)
        Some(What)
        Some(World!)
        Some(Hello)
        Nothing
"""

"""
Exercise 4: The "Trait-like" Interface (Abstract Base Classes)

In Rust, you cant instantiate a Trait. In Python, you can accidentally instantiate a base class unless you use ABCs.

The Task: Create a Shape interface that enforces specific methods at "compile time" (startup).

    Requirements:

        Import from abc import ABC, abstractmethod.

        Define a class Shape(ABC).

        Mark area(self) and perimeter(self) as @abstractmethod.

        Create a Circle and Square subclass.

        The Test: Try to create an instance of Shape(). Python should raise a TypeError. This is the closest Python gets to a Rust Trait requirement.
"""
from abc import ABC, abstractmethod
from math import pi
class Shape(ABC): #ABC = Abstract Base class

    @abstractmethod
    def area(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def perimeter(self) -> int:
        raise NotImplementedError
#shape = Shape() <- TypeError: Can't instantiate abstract class Shape without an implementation for abstract methods 'area', 'perimeter'

class Square(Shape):
    def __init__(self, len: int):
        self.length = len
    def area(self) -> int:
        return self.length ** 2
    def perimeter(self) -> int:
        return self.length * 4
# shape = Square(6)
# print(shape.area(), shape.perimeter()) <- 36 24
class Circle(Shape):
    def __init__(self, radius: int):
        self.r: int = radius

    def area(self) -> int:
        return self.r * self.r * pi
    def perimeter(self) -> int:
        return 2 * pi * self.r
# shape = Circle(1/pi)
# print(shape.area(), shape.perimeter()) <- 0.3183098861837907 2.0

"""
Exercise 5: The "Smart Pointer" (Context Managers)

In Rust, Drop is called when a variable goes out of scope. In Python, we use the with statement (Context Managers) to handle resource cleanup.

The Task: Create a DatabaseConnection class that mimics RAII.

    Requirements:

        Implement __enter__(self): This should print "Connecting to DB..." and return self.

        Implement __exit__(self, exc_type, exc_val, exc_tb): This should print "Closing Connection safely."

        Add a method execute(self, query: str).

        The Test: Use the with keyword to initialize the class. Verify that even if an error occurs inside the with block, the "Closing Connection" message still prints.
"""

## I do not have enough knowledge about Databases to implement this. So skipping.ABC

"""
Exercise 6: The "Registry" (Metaclasses or Class Decorators)

This is "Advanced Python" territory. In Rust, you might use a procedural macro to register types. In Python, we can use a Class Decorator.

    The Task: Create a decorator that "registers" every class it is applied to into a global dictionary.

    Requirements:

        Create a dictionary PLUGIN_REGISTRY = {}.

        Create a function register_plugin(cls).

        Inside that function, add the class name as a key and the class itself as the value to the dictionary. Return the class.

        Use @register_plugin on several classes (e.g., AudioPlugin, VideoPlugin).

        The Test: Print PLUGIN_REGISTRY to show that the classes "self-registered" just by being defined.
"""
PLUGIN_REGISTRY = {}
def register_plugin(plugin_class):
    name = plugin_class.__name__
    PLUGIN_REGISTRY[name] = plugin_class
    return plugin_class

@register_plugin
class AudioPlugin:
    def __init__(self):
        self.dummy = None
@register_plugin
class VideoPlugin:
    def __init__(self):
        self.dummy = None
#print(PLUGIN_REGISTRY)
"""
PLUGIN_REGISTRY:
{
    'AudioPlugin': <class '__main__.AudioPlugin'>,
    'VideoPlugin': <class '__main__.VideoPlugin'>
}
"""

"""
Exercise 7: The "Newtype" Pattern (Properties & Slots)

In Rust, we use the Newtype pattern for safety (e.g., struct Celsius(f64)). In Python, we can use __slots__ for memory efficiency and @property for validation.

The Task: Create a Temperature class that stores values in Kelvin internally but exposes Celsius.

    Requirements:

        Use __slots__ = ("_kelvin",) to prevent the creation of a dynamic __dict__ (this makes the class much smaller in memory, like a Rust struct).

        Create a @property called celsius. It should calculate the value from the internal _kelvin.

        Create a @celsius.setter. If the user tries to set a temperature below absolute zero (−273.15°C), raise ValueError.
"""
class Celsius:
    __slots__ = ("_kelvin",)
    def __init__(self, celsius: int):
        self._kelvin = celsius + 273.15

    @property ## <- This attribute gets run when getting a value. Basically making a field.
    def celsius(self):
        return self._kelvin - 273.15

    @celsius.setter ## <- This gets run when it is getting set.
    def celsius(self, value):
        __temp__kelvin__ = value + 273.15
        if __temp__kelvin__ < 0:
            raise ValueError("Temperature Cannot be below absolute zero.")
        self._kelvin = __temp__kelvin__
"""CODE:
temperature = Celsius(30)
print(f"Temperature: {temperature.celsius}")
temperature.celsius = 40
print(f"Temperature: {temperature.celsius}")
"""
"""OUTPUT:
Temperature: 30.0
Temperature: 40.0
"""
temperature = Celsius(0)
print(f"Temperature: {temperature.celsius}")
temperature.celsius = -274.15
print(f"Temperature: {temperature.celsius}")

