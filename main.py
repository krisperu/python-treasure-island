print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

step1 = input("You are stroling through a lush magical forest. The birdsong and rustling of the leaves create a lovely symphony as you reach a fork in the road. Which way do you go? Left or Right? \n").lower()
if step1 == "left":
  step2 = input("Soft golden light is filtering through luscious trees, creating funky patterns on the cobblestone path. You're humming a jaunty tune and hear a rushing noise. A river!! Its time to decide, do you swim through it or find a way around it? Swim or Avoid? \n").lower()
  if step2 == "avoid":
    step3 = input("A mile of rushing river and stony coast brings you to a shrap curve. Rounding the corner, you are met with a beautiful log cabin, and a bridge across the river. As you're crossing the bridge you notice a gnarled old tree that looks older than anything you've seen all day. As you start walking toward it you notice that the cabin has an intricate door that seems to be calling your name. You turn away to try to decide what to do and notice an old dilapidated shed peeking through the trees. Almost as if no one wanted it to be seen. Which thing do you want to  investigate first? Tree, Shed, or Cabin? \n").lower()
    if step3 == "tree":
      print("Slowly, you start walking towards the tree. The trunk is so wide your hands can't reach around it. There's a little hole near the bottom of the trunk and a shovel next to it. You pick up the shovel and start digging. Thunk! Congratulations! You have found the hidden treasure.")
    elif step3 == "shed":
      print("You make your way past the trees and to the shed. You jimmy open the door and walk in. It's so dark. You take two steps. AGHH! You fall into a hole and die! Game over. :(")
    elif step3 == "cabin":
      print("You take two steps toward the cabin when a huge thunderbird swoops down and flies you to it's nest and feeds you to its kids. Game Over. :(")
  else:
    print("Splash! You jump in the water. Whoosh! The strong current takes you away. You're fighting with tooth and nail to stay afloat when OUCH! Shomething bites you! Two seconds later your dead and the snake that bit you swims away happily. Game over. :(")
else:
  print("After walking about three miles a weird growling sounds seems to start follwoing you. You pick up your pace and get deeper into the woods. Your hair starts to stand on end and the growling seems to grow closer. SNAP! That was defintley a branch breaking behind you! You start to run and turn your head to see who is follwoing. The bush is shaking, the wind is howling, and you start sweating through your shirt. Phew! It was just a fox! You start laughing! How silly! You turn around to contiue and find yourself surrounded by thousands of spiders. They swarm up your legs and devour you whole within seconds. Game Over. :(")
