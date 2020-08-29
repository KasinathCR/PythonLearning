#Print the Greatest Common Divisor between 2 Inputs(Euclid's Algorithm)
def GCD(a, b):
    while(b != 0):
        t = a;
        a = b;
        b = t % b;
    return a;

print(GCD(60, 96)); #Prints 12
print(GCD(20, 8)); #Prints 4
