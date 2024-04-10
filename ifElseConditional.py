# age = int(input("Enter you age: "))
# print(age)

# if(age >= 18) :
#     print('you are eligible for vote')
# else :
#     print('you are eligible for vote')


applePrice = int(input("Enter price of 1Kg Apple: "))
budget = int(input("Enter your budget: "))

if(applePrice == budget):
    print("you can buy 1 kg Apple");
elif(applePrice < budget):
    print("you can buy more than 1 kg of apple")
elif(budget == 0):
    print("you can not buy any apple");
else:
    print("you can buy less than 1 kg of apple") 
