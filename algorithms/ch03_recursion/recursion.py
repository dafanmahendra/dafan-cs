# def countdown(time):
#    print(time)

#    if time <= 1: # base case
#        return
#    else:
#        countdown(time - 1) # recursive case
    
# countdown(5)

# di atas itu kodingan yang bener supaya engak error, kalo di atas itu kodingan yang salah karena ada komentar countdown(time - 1) yang bikin error

# call stack 

def greet(name):
    print("hello, " + name + "!")
    greet2(name)
    print("getting ready to say bye!")
    bye()

def bye():
    print("ok, goodbye!")

# 2 functions 

def greet2(name):
    print("hello again, " + name)
    
greet("mario")





