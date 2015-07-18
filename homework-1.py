#This is a test for an abstract homeword
stud_id = input('Enter your name and surname seperated by a space (First Letters of name and surname in uppercase): ')
w = []
question1 = 'What is the sum of all the angles of a triange?'
print(question1)
answer1 = int(input('Give your answer: '))
if (answer1 == 180):
	w.append(50)
question2 = 'How many sides does a pentagon have?'
print(question2)
answer2 =  int(input('Give your answer: '))
if(answer2 == 5):
	w.append(50)
grade = sum(w)
print('Your grade is: {}%'.format(grade))
#generator of code to be submitted
def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result
#continue with the algorithm
key = len(tobits(stud_id))*100
print("Dear {} send the following characters at pgeorgios8@gmail.com in order for me to receive your grade: {}{}{}".format(stud_id,chr(key),chr(key+grade),chr(grade%key)))
