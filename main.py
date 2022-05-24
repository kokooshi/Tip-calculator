print ("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
percent = input ("What percentage tip would you like to give?10, 12, or 15?")
people= input ("How many people to split the bill?")
# convert to int
a= float (bill)
b= int (percent)
c= int (people)
#formula
r= a * b/100 +a
final= r/c
f= round (final,2)
f= "{:.2f}".format(final)
print (f"Each person should pa: ${f}.")