shows = ["Dexter", "The Office", "9-1-1"]

need_to_watch = ["TMS", "ASIP"]

all_shows = []

'''
while input('y or n?') != 'n':
  for i in range(1,6):
    print(i)


for i in range(1,3):
  print(i)
  for letter in ["a", "b", "c"]:
    print(letter)


for show in shows:
  show = show.upper()
  all_shows.append(show)

for show in need_to_watch:
  show = show.upper()
  all_shows.append(show)

print(all_shows)

x = 10
while x > 0:
  print('{}'.format(x))
  x -= 1
print("Happy New Year!")

qs = ["What is your name?", "What is your fav. color?", "What is your quest?"]

n = 0
while True:
  print("Type q to quit.")
  a = input(qs[n])
  if a == "q":
    break
  n = (n + 1) % 3
 

for i, show in enumerate(shows):
  new = shows[i]
  new = new.upper()
  shows[i] = new

print(shows)
'''

