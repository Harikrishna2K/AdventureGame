
print("welcome to my first game")
name = input("Enter the name ")
age = int(input("Enter the age "))
health = 10 

if age >= 18:
  
  print("You are grown enough to play")

  want_to_play = input("DO you want to play this game? ")
  
  if want_to_play == "yes":
     print("you are starting with ", health, "health")
     print("Lets start to play this game")

     left_or_right = input("Do you want to move left or right, (left/right) " )
     if left_or_right == "left" :
       ans = input("You are running in the house ,do you want to move across or around the home,(across /around" ) 
        
       if ans == "around":
            print("Yes its the time to move left for survival,but you  managed to go through..")
        
       elif ans == "across":
           print("Yes this the time you lost by getting hit by the enemy")
           health -= 5
       ans = input("you notice there is a house and river to go, where will you go (house/river)?:  ")
       
       if ans == "house":
            print("You are beaten by the owner ")
            health -= 5 
 
            if health <= 0:
                print("The game is lost as you have no health remaining")
            else:
                 print("you have survived la la la .....")
       else :
            print("you lose the game by falling into the river")
       
     else :
             print("you are lost bye bye ")
  
  
  else:
       print("bye")
else:
  print("You are not enough to play")
