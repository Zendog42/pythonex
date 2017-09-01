print("What is the first integer?", end=' ')
int_x = int(input())

print("What is the second integer?", end=' ')
int_y = int(input())

print("What is the operation?", end=' ')
op = input()

if(op == "+"):
    answer = (int_x + int_y)
elif(op == "-"):
    answer = (int_x - int_y)
elif(op == "*"):
    answer = (int_x * int_y)
elif(op == "/"):
    answer = (int_x / int_y)
else:
    print("Nah, that's fucked up")
 
print(f"{int_x} {op} {int_y} = {answer}.")
