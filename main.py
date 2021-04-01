# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#writeing a bmi calculator  that will print if you are, underweight, overweight, or obese
bmi_weight = float(weight)
bmi_height = float(height)**2
bmi = round(bmi_weight / bmi_height)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi > 18.5 and bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi > 25 and bmi < 30:
  print("Your BMI is 28, you are slightly overweight.")   
elif bmi > 30 and bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")  

