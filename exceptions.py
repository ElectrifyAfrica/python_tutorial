try: 
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
    print("")
except ValueError:
   print('InvalidValue')
   print("")



try: 
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("age can't be Zero \nCan't divide by Zero")
except ValueError:
   print('InvalidError')
   
   