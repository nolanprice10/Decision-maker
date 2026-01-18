import random

decisions = []

while True:

  choice = input("type a decision; type DONE to finish: ")
  if choice == "DONE":
    break
  decisions.append(choice)
if len(decisions) == 0:
  print("you have to actually add a decision lol")
  exit()
result = random.choice(decisions)
print("how about...", result)
