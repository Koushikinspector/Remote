import csv

# opening the CSV file
with open('BMSData.csv', mode ='w')as file:
	writer = csv.writer(file)
	writer.writerow(["Lorem","Horror","1hr 20mins","John doe","Moon F","5/10","English","8,10.05,12.10,2.15,4.20","5","8AM","15mins","30mins","50"])

with open('BMSData.csv', mode='r') as file:
	reader = csv.reader(file)
	count=0
	for row in reader:
		print(row)
global f
f = 0

def t_movie():
	global f
	f = f+1
	print("welcome to user1")
	print("1,Book your ticket")
	print("2,Cancel your ticket")
	print("3,Give user rating")
	movie = int(input("choose your option: "))
	if movie == 1:
		timings()
	return 0


# this theater function used to select screen
def timings():
	print("What timings do you want choose ")
	print("1,8-12")
	print("2,1-3")
	time = int(input("choose your Timings: "))
	if time==1:
		print("only 15 tickets are available")
	if time==2:
		print("only 30 tickets are available")
	ticket = int(input("number of ticket do you want?: "))
		if ticket >30:
			print("Availablle tickets only 30")
		elif ticket <=30:
			print("Your "+ticket + "tickets has successfully Booked")
			

	print("Thanks for booking")
t_movie()

