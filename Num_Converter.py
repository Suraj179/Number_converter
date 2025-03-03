
dic={0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
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
        remainder_str=dic[remainder]
        answer1=remainder_str+answer1
        number1=(number1-remainder)/base
    
    #converting decimal part
    answer2="."
    while number2!=0:
        product=number2*base
        pro_int=int(product)
        pro_str=dic[pro_int]
        answer2+=pro_str
        number2=product-pro_int
    try:
        answer1=int(answer1)
        answer2=float(answer2)
        if answer1!=0:answer+=answer1
        if answer2!=0:answer+=answer2
    except ValueError:
        answer=""
        if answer1!="":answer=answer+answer1
        if answer2!=".":answer=answer+answer2
    return answer
# num=float(input("Enter the number: "))
# base=int(input("Enter the base: "))
# print(decimal_base(num,base))

def base_decimal(number,base):
    #get the maximum exponent or highest power
    integer=number.split(".")[0]
    highest_power=len(integer)-1
    print(highest_power)
    dic2 = {v: k for k, v in dic.items()}
    answer=int()
    for i in number:
        if i==".":continue
        num=dic2[i]
        answer+=num*base**highest_power
        highest_power-=1
    
    print(answer)

base_decimal("154724.6543177",8)