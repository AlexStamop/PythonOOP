class Flower: #Creating a class named flower
    def __init__(self, name): #Using init function to assign the name
        self.name = name #Setting the name

    def grow(self): #Defining a function grow that prints the name is growing
        print("The " +self.name + " is growing.") #Printing out the name and is growing

    def bloom(self): #Defining a function bloom that prints the name is blooming
        print("The " + self.name + " is blooming.") #Printing the name is blooming

def main(): #Defining the main program
    flower1 = Flower("Rose") #Running the flower class and setting the name as rose
    flower1.grow() #Running the object grow
    flower1.bloom() #Running the object bloom
    flower2 = Flower("Daisy") #Running the object flower and setting the name as Daisy
    flower2.grow() #Running the object grow
    flower2.bloom() #Running the object bloom

if __name__ == "__main__": #Conditional if statement assigning the string name
  main() #Running the main program