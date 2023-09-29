# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
	MObject is an abstract class as it acts like a blueprint or parent/base class for the child classe image.
2. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	'__del__' class method is basically a destructor used to delete the base class instance. As referred in (https://docs.python.org/3/reference/datamodel.html#object.__del__), it destructs the base class instance and only calls it once.
3. What class does Texture inherit from?
	The class Texture inherits from Image class.
4. What methods and attributes does the Texture class inherit from 'Image'? 
	It inherits width and height and pixels and getPixelColorR and setPixelsToRandomValue from base Image.
5. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	Yes the image should have a 'has-a' relationship to the texture and the code is refactored. According to the code the object of the image is passed as a reference to the Texture class through which it can access the functions of the  image class.
6. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	Yes.

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?

There are few egde cases where the instance is none is a thread and another thread is calling the super instance where two objects gets created thus using a lock would be a better option.
 
  
