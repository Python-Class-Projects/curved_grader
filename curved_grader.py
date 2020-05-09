import math
#42 spaces. Will print introduction header.
def introduction_header(): 
	print("*" * 42)
	print("{title:^42}".format(title = "CURVED GRADE CALCULATOR"))
	print("*" * 42)

#42 spaces. Will print course header for average printing. 
def course_header(): 
	print("{title: ^42}".format(title = "*Course Final Grades Report*"))
	print("{name:<14}{average:^14}{grade:>14}".format(name = "Name", average = "Average", grade = "Grade"))
	print("-" * 42)
	print()
#26 spaces, prints the summary heading
def summary_header():
	print("{summary:^26}".format(summary = "Summary"))
	print("-" * 26)
#Finding the mean by dividing the total averages scores to the amount of accumulated averages.
def find_mean(tot_averages,accum_averages):
	mean = tot_averages / len(accum_averages)
	return mean

#Median
#Will find the median. Copying the list, avoiding referencing the object. Then sort the copied list, and finding the middle value for the median.
#If it is an odd list, then we take the two middle values in the list, add them and divide by two to find the median.
def find_median(accum_averages):
	if len(accum_averages) % 2 == 1:
		copy_list = list(accum_averages)
		copy_list.sort()
		median = copy_list[int(len(copy_list)) // 2]
		return median

	else: 
		copy_list = list(accum_averages)
		copy_list.sort()
		position = len(copy_list) // 2
		high = copy_list[position]
		low = copy_list[position-1]
		median = (high + low) / 2
		return median
#Variance
def find_variance(vals):
	mean = find_mean(tot_averages,accum_averages)
	total = 0 

	for val in vals:
		total = total + (val-mean)**2
	variance = total / len(vals)
	return variance

#Find population standard deviation
def find_stdev(vals):
	return math.sqrt(find_variance(vals))

#finds min by sorting a copy of the accum_averages
def find_min(accum_averages):
	copy = list(accum_averages)
	copy.sort()
	minimum = copy[0]
	return minimum
#Finds max by sorting a copy of the accum_averages
def find_max(accum_averages):
	copy = list(accum_averages)
	copy.sort()
	maximum = copy[-1]
	return maximum
#Obtaining grade letter to print and appending letter lists with the respected letter grades. 
def find_letter_grade(accum_averages,stdev,mean):
	letters = []

	for val in accum_averages:
		if val >= mean + (1.25 * stdev):
			letters.append("A")
		elif val >= mean + (0.25 * stdev):
			letters.append("B")
		elif val >= mean - (1 * stdev):
			letters.append("C")
		elif val >= mean - (2 * stdev):
			letters.append("D")
		elif val < mean - (2 * stdev):
			letters.append("F")
	return letters
#Gets the letter frequencies using a libary. 
def get_letter_frequencies(letters):
	freqs = {}

	for letter in letters:
		if letter in freqs:
			freqs[letter] = freqs[letter] + 1
		else:
			freqs[letter] = 1
	return freqs
#find mode in the letters list
def find_mode(letters):
	mode = []
	freqs = {}
	most = 0
	for letter in letters:
		if letter in freqs:
			freqs[letter] = freqs[letter] + 1
		else:
			freqs[letter] = 1
			
		if freqs[letter] > most:
			most = freqs[letter]
	for letter in freqs:
		if freqs[letter] == most:
			mode.append(letter)
	return mode[0]

#Code that prints the output of final results. This will take all values in parameters after the end of the program when all
#variables are found.
def summary_header(mean,median,stdev,minimum,maximum,mode,frequencies):
	print("\n{summary:^20}".format(summary = "Summary"))
	print("-" * 20)
	print("{Mean:<10}{mean:>10.2f}".format(Mean = "Mean", mean = mean))
	print("{Median:<10}{median:>10.2f}".format(Median = "Median", median = median))
	print("{StDev:<10}{stdev:>10.2f}".format(StDev = "StDev", stdev = stdev))
	print("{Minimum:<10}{minimum:>10.2f}".format(Minimum = "Minimum", minimum = minimum))
	print("{Maximum:<10}{maximum:>10.2f}".format(Maximum = "Maximum", maximum = maximum))
	print("{common:<10} {mode}".format(common = "Most common grade:", mode = mode))
	print("{number_of:<10}{frequencies:>10}".format(number_of = "# of A's", frequencies = frequencies['A']))
	print("{number_of:<10}{frequencies:>10}".format(number_of = "# of B's", frequencies = frequencies['B']))
	print("{number_of:<10}{frequencies:>10}".format(number_of = "# of C's", frequencies = frequencies['C']))
	print("{number_of:<10}{frequencies:>10}".format(number_of = "# of D's", frequencies = frequencies['D']))
	print("{number_of:<10}{frequencies:>10}".format(number_of = "# of F's", frequencies = frequencies['F']))
	print("Thank you for using this program.")

#print introduction header
introduction_header()
file = input("Enter name of test scores file: ")
print("test_scores.txt\n")
course_header()
myfile = open(file,"r")
first_line = True #initialize this variable and set it to true, but will change to flase after first iteration.
accum_students = []#List to hold all students
average = 0 #Initializing average
accum_averages = [] #List that holds the averages of all students
tot_averages = 0 #variable that will iterate through a for loop to obtain the total number of the accumalated average scores.
mean = 0 #variable that after obtaining the total_averages, will find the mean by tot_averages / len(accum_averages)
median = 0 #Initializing median
for line in myfile: #looping through file. 
	if first_line == False:
		line = line.strip()
		parts = line.split("\t")  #will contain the part seperated by a tab.

		#Get all student_num, averages, and grade letters
		#This if statement will determine the data line without "F10" being present on parts[5], which is the last test score.
		#The elif statement will determine the data line with the "F10" being present on parts[5] to remove the "F10" and keep the score only.
		if "Student_" in parts[0] and "F10" not in parts[5] : #This will check if parts begin with row "Student_" to seperate data with title.
			students = parts[0]
			accum_students.append(students)
			scores = [int(i) for i in parts[1:]]
			average = float(scores[0] + scores[1] + scores[2] + scores[3] + scores[4]) / 5 #Getting the average by dividing the scores in list by how many elements (test scores).
			accum_averages.append(average) #Will append the average to the accum_average list to later find the mean.


		elif "Student_" in parts[0] and "F10" in parts[5]: 
			students = parts[0]
			accum_students.append(students)
			scores = [int(i) for i in parts[1:5]]
			score_with_letter = parts[5][0:2] #Accessing student_9 because of elif condition, then retrieving the first two string characters, removing "F10."
			scores.append(int(score_with_letter)) #Appending the score after removing "F10" and then converting the first two digits "87" into an integer to append to scores.
			average = float(scores[0] + scores[1] + scores[2] + scores[3] + scores[4]) / 5 #Getting the average by dividing the scores in list by how many elements (test scores)
			accum_averages.append(average) #Will append the average to the accum_average list to later find the mean.


	first_line = False
myfile.close()

#This will obtain the total number of averages in the loop stored into tot_averages.
for i in accum_averages:
	tot_averages += i
#Mean
mean = find_mean(tot_averages,accum_averages)

#Median
median = find_median(accum_averages)

#Variance
variance = find_variance(accum_averages)

stdev = find_stdev(accum_averages)

#Minimum
minimum = find_min(accum_averages)

#Maximum
maximum = find_max(accum_averages)


#Obtaining grade letter to print and appending letter lists with the respected letter grades. 
letters = find_letter_grade(accum_averages,stdev,mean)

#Printing the student columns and rows. Will print the student, average for student and letter grade received for each student.
for index in range(len(accum_students)):
	print(f"{accum_students[index]:<14}{accum_averages[index]:^14.2f}{letters[index]:>14}")

#Frequency
frequencies = get_letter_frequencies(letters)

#Most common grade
mode = find_mode(letters)

#Print the summary
summary_header(mean,median,stdev,minimum,maximum,mode,frequencies)
