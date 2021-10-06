#find the avergae of numbers in a text file
#call the libriary for regex
import re
#declare the variables 
sum1=0
count=0
avrg=int()
#open the file text 
fh=open('mbox-short.txt')
#read the file text
for line in fh:
    line=line.rstrip()
    #extract all the numbers in New Revision line
    x=re.findall('^New Revision: ([0-9]+)',line)
    #a loop to eleminate from the list non numbers (if they are)
    if len(x)>0:
        #look through the new list with numbers
        for nr in x:
            #find the sum of the elements of x list and count them
            sum1=sum1+int(nr)
            count=count+1
        #find the average as an integer number
        avrg=int(sum1/count)
#print the average
print(avrg)