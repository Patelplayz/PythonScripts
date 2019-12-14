import csv

with open('attempot.csv') as file:
   reader = csv.DictReader(file)

   count = 0

   for row in reader:
       print(row['Birth Date'])

       if count > 5:
           break

count += 1

