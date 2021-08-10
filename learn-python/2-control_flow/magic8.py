name = input("Enter name here: ")
question = input("Enter question here: ")
answer =  ""

if len(name) == 0:
  print("Question: " + question)
else:
  print(name + " asks: " + question)
if len(question) == 0:
  print("The Magic 8-Ball cannot provide a fortune unless you ask it something.")

import random
random_number=random.randint(1,12)

if random_number== 1:
  answer= "Yes - definitely"
elif random_number== 2:
  answer="It is decidedly so."
elif random_number== 3:
  answer="Without a doubt."
elif random_number== 4:
  answer="Reply hazy, try again."
elif random_number== 5:
  answer="Ask again later."
elif random_number== 6:
  answer="Better not tell you now."
elif random_number== 7:
  answer="My sources say no."
elif random_number== 8:
  answer="Outlook not so good."
elif random_number== 9:
  answer="Very doubtful."
elif random_number == 10:
    answer="100% definitely! Congrats very pog."
elif random_number == 11:
    answer="You will see with time."
elif random_number == 12:
    answer="The future is uncertain. Try again."
else:
  "Error"
if len(question) == 0:
  answer="error"
else:
  print("Magic 8-Ball's answer: " + answer)