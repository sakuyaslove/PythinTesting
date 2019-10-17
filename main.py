print("Hello and welcome to our beta Choose Your Own Adventure game.")
pName = input("But first, what is your name? ")
pName = pName.capitalize()
print("-----")
print("Hi", pName)
print("Now, what is your favorate food from these options:")
print("A: Pizza")
print("B: Burgers")
print("C: Tacos")
favFood = input("Type the letter to answer: ")
favFood = favFood.capitalize()
print("-----")
while (favFood != "A" and favFood != "B" and favFood != "C"):
  print("Sorry, you have to type A or B or C and hit ENTER to make your selection")
  print("Now, wh  at is your favorate food from these options:")
  print("A: Pizza")
  print("B: Burgers")
  print("C: Tacos")
  favFood = input("Type the letter to answer: ")
  favFood = favFood.capitalize()
  print("-----")
if favFood == "A":
  favFood = "Pizza"
  print("MMMmmmm, I love", favFood, "too!")  
elif favFood == "B":
  favFood = "Burgers"  
  print("MMMmmmm, I love", favFood, "too!")
elif favFood == "C":
  favFood = "Tacos"  
  print("MMMmmmm, I love", favFood, "too!")
print("-----")
