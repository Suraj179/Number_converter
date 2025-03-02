

def decimal_base(number:float,base:int):
    number1=int(number)
    round_of_number2=len(str(number))-len(str(number1))
    number2=round(number%1,round_of_number2)
    
    print(f"number: {number}\nnumber1: {number1}\nnumber2: {number2}")
    answer=int()

    #converting integer part
    answer1=""
    while number1!=0:
        remainder=int(number1%base)
        remainder_str=str(remainder)
        answer1=remainder_str+answer1
        number1=(number1-remainder)/base
    
    #converting decimal part
    answer2="0."
    while number2!=0:
        product=number2*base
        pro_int=int(product)
        pro_str=str(pro_int)
        answer2+=pro_str
        number2=product-pro_int

    answer1=int(answer1)
    answer2=float(answer2)
    if answer1!=0:answer+=answer1
    if answer2!=0:answer+=answer2
    return answer
# num=float(input("Enter the number: "))
# base=int(input("Enter the base: "))
print(0==0.0)
i=True
while i:
    num=float(input("Enter the number: "))
    base=int(input("Enter the base: ")) 
    print(decimal_base(num,base))
    i=input("enter truth value: ")

