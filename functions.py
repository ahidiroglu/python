def whatareyou(num1, num2):
    return num1 + num2

def division(num1, num2):
    if num2 == 0:
        return "ERROR: Cannot divide by Zero"
    else:
        return num1/num2
var1 = 10
var2 = 15
var3 = 576

result = whatareyou(var1, var2)
print("Result of addition:", result)

result = division(var3, var2)
print("Result of division:", result)
     