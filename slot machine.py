import random 
print("I'am a prediction machine you have to predict the numbers 1 , 2 , 3. if you are lucky and the answer is correct you win. if you want to continue write 'cool' ")
application=str(input())
if application=="cool":
  print("let's begin")
else :
  print("ok, Bye")
  exit()
print("select a number between 1 , 2 , 3😊")
answer = int(input())
ans=random.randint(1,3)
if answer==ans:
  print("you win")
else:
  print("sorry😢😢")