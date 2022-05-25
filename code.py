import math

def convretToBinary(num):
    result = ""
    if num < 1:
        counter = 0
        while num != 0 and counter <23:
            num = num * 2
            if(num >= 1):
                num = num - 1
                result += "1"
            else:
                result += "0"
            counter += 1
        return result

    result = bin(int(num))
    result = result.replace("0b", "")
    return result

def caclulateMantisaAndExponent(num): #num is in string format
    exponent = num.index(".") - 1 #exponent = index number of dot - 1
    num = num.replace(".", "")
    num = num[1:]
    while len(num) < 23:
        num = num + "0"
    exponent = bin(exponent + 127).replace("0b", "")
    return [num, exponent]

#________________________main________________________
while True:
    try:
        number = float(input("input float-number that you want to show as IEEE 754 : "))
        break
    except:
        print("please input number ...")
signBit = "0"
if number < 0:
    signBit = "1"
tupleOfNumber = math.modf(abs(number)) #tupleOFNumber = (fractional parts of x, integer parts of x)
fixedPointNumber = convretToBinary(tupleOfNumber[1]) + "." + convretToBinary(tupleOfNumber[0])
#print(fixedPointNumber)
numAndExponent = caclulateMantisaAndExponent(fixedPointNumber)
print(signBit + "|" + numAndExponent[1] + "|" + numAndExponent[0])