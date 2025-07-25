#Code Notes: You want three outputs. The flower (not filled), a filled flower with 6 different colors, and a spiraled star

#importing turtle.
import turtle

#function for flower shape
def draw_square(square):
    for i in range(0, 2):
        square.forward(100)
        square.right(70)
        square.forward(100)
        square.right(110)

#function to draw the flower
def draw_flower(petal_number: int):
    """Draws a flower on the screen with a given number of petals
    :param petal_number: 
    :return: Blocks until the user clicks on the screen"""
    window = turtle.Screen()
    window.bgcolor("beige")
    window.title("Flower")
#flower turtle
    flower = turtle.Turtle()
    flower.shape("triangle")
    flower.color("teal")
    flower.pencolor("beige")
    flower.pensize(3)

    flower.goto(15,70)

    for number in range(0, petal_number):
        flower.begin_fill()
        draw_square(flower)
        flower.end_fill()
        flower.right(360.0 / petal_number)

    window.exitonclick()
#when clicked the window closes

#function for colorful art (the petals are filled in with different colors)
def colorfulArt(numberOfPetals):
   colors = ["red","blue","green","orange","pink","teal","purple","yellow"]
   window = turtle.Screen()
   window.bgcolor("white")
   window.title("Pinwheel Flower")

   flower = turtle.Turtle()
   flower.shape("triangle")
   flower.color("blue")

   for petalNumber in range(numberOfPetals):
      flower.begin_fill()
      flower.color("white",colors[petalNumber%8])
      draw_square(flower)
      flower.end_fill()
      flower.right(360.0/numberOfPetals)

   window.exitonclick() #when clicked the window closes

#function for original art(which is just stars)
def originalStars(n):

   window = turtle.Screen()
   window.bgcolor("white")
   window.title("Star Power")

   star_spiral = turtle.Turtle()
   star_spiral.begin_fill()
   star_spiral.shape("triangle")
   star_spiral.color("teal")
   for count in range(20+n):
       star_spiral.forward(count*15)
       star_spiral.right(144)
       star_spiral.end_fill()
   window.exitonclick()

#let the user choose
print("Choose from the following:")
print("1. Flowers.")
print("2. Colorful Flower.")
print("3. Spiraled Star.")
UserChoice = int(input())

#if statement check the user choice
if (UserChoice == 1):
   numberOfPetals= int(input("How many petals?"))
#the next line calls the draw flower function
   draw_flower(numberOfPetals)
#elif- chapter 5 conditional statement
elif(UserChoice == 2):
   numberOfPetals = int(input("How many petals?"))
   colorfulArt(numberOfPetals) #this line calls the colorful art function
else:
   (UserChoice == 3)
   numberOfPetals= int(input("How many stars should overlap?"))
   originalStars(numberOfPetals) #this line calls the original stars function