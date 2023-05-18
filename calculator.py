import math

while True: 
    
    in1 = input("Choose either 'investment' or 'bond' from the menu below to proceed: \n\nInvestment - to calculate the amount of interest you'll earn on your investment.\nBond - to calculate the amount you'll have to pay on a home loan.\n\ninput choice here:")
    if in1.lower() == "investment":
        inDeposite = int(input("Please input the amount of money that you are investing.\nHere: "))
        inInterestRate = int(input("Please input the interest rate  (as  a  percentage).  Only  the  number of the interest rate should be entered\n Here:"))
        inYears = int(input("Please input the number of years you plan on investing for.\nHere: "))
        intrest = input("Would you like simple intrest or compound intrest (only input 'simple' or 'compound').\n Here:")
        intrestSimple = inDeposite * (1 + (inInterestRate/100) * inYears)
        intrestCompound = inDeposite * math.pow( (1 + (inInterestRate/100) ) , inYears)
        if intrest.lower() == "simple":
            print("Simple intresr after",inYears,": R",intrestSimple)
        elif intrest.lower() == "compound":
            print("Compound interest after",inYears," years: R",intrestCompound)
        else:
            print("invalid input")
    
    elif in1.lower() == "bond":
        bopresentValue = int(input("Please input the present value of the house.\n Here:"))
        boIntrestRate = int(input("Please input the interest rate  (as  a  percentage).  Only  the  number of the interest rate should be entered\n Here:"))
        i = float(boIntrestRate/12)
        boMonths = int(input("Please input the number of months you plan to take to repay the bond.\n Here:"))
        boFormula = ((i/100) * bopresentValue) / (1 - math.pow((1 + i/100), -boMonths))

        print("Your monthly instalment will be R",boFormula,"each month")  
    
    else:
        print("invalid input")
        break
    