# Create a funtion called mark_grade to hold user grade input and IF statement to advise what grade the user got. 
def mark_grade():
  mark_grade = int(input("What % of 100 did you get in the test? "))
# Create IF statement to interpret the input and present a statement advising the user of their grade
  if (mark_grade >= 85):
    print ("WOAH, you got an A?! Gold star for you!")
  elif (mark_grade >=75 and mark_grade <85):
    print ("Nice work, B is a really good grade.")
  elif (mark_grade>= 65 and mark_grade<75):
    print ("C is a good grade.")
  elif (mark_grade >= 55 and mark_grade <65):
    print ("Grade D, that's not great.")
  elif (mark_grade >=0 and mark_grade <55):
    print ("That's a fail, you'll have to re-sit.")
  
  else:
    print ("You and I both know that's not the answer I was looking for.")


  target_grade = int(input("And, what was your target % ? "))

  if target_grade < mark_grade:
    print ("Your achieved grade is over your target grade. Well done!")
  elif target_grade == mark_grade:
    print ("Congratulations! You hit your target grade!")
  elif target_grade > mark_grade:
    print ("That's unfortunate, you didn't achieve your target grade.")

mark_grade()
