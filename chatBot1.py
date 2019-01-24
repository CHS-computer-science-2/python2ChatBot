#This is the starter code for the Chatbot
# <Your Name Here>
#This is a chatbot and this is a comment, not executed by the program
#Extend it to make the computer ask for your favorite movie and respond accordingly!

def main():
    print('Hello this is your computer...what is your favorite number?')
    #Declaring our first variable below called 'computerfavnumber' and storing the
    #value 33
    computerfavnumber=33
    #We now declare a variable but set the variable to hold whatever the *user*
    #inputs into the program
    favnumber = input("Number please: ")
    print(favnumber + '...is a very nice number indeed. So...what is your name?')
    name=input()
    print('what a lovely name:  ' + name + '...now, I will reveal what my favourite number is:')
    print (computerfavnumber)

main()
