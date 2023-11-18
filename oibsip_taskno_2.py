def height(height_scale):
    if height_scale == "feet":
        height_feet = int(input(f"Enter your Height in {height_scale}: "))
        height_inches = int(input(f"Enter your inches: "))
        height = height_feet*12+height_inches
        return height
    elif height_scale == "cm":
        height_cm = int(input("Enter your height in cm: "))
        return height_cm
    else:
        print("Invalid Scale!! Choose between cm/feet")

def weight(weight_scale):
    if weight_scale in ["Pounds","Kgs"]:
        weight = int(input(f"Enter your weight in {weight_scale}: "))
        return weight
    else:
        print("Invalid Scale!! Choose between Pounds/Kgs")

def main():
    height_scale = input("Enter Scale for height (cm/feet): ")
    weight_scale = input("Enter Scale for weight (Pounds/Kgs): ")
    bmi = 0

    main_height = height(height_scale)
    main_weight = weight(weight_scale)

    if height_scale == "cm" and weight_scale == "Kgs":
        main_height = main_height/100
        bmi = (main_weight/(main_height)**2)
        print("Your BMI is: ",bmi)
    elif height_scale == "feet" and weight_scale == "Pounds":
        bmi = (main_weight/(main_height)**2)*703
        print("Your BMI is: ",bmi)
    else:
        print("Choose a combination of cm and Kgs or feet and Pounds")

    if 0<bmi<18.5:
        print("Underweight")
    elif 18.6<bmi<24.9:
        print("Healthy Weight")
    elif 25<bmi<29.9:
        print("Overweight")
    elif 30<bmi:
        print("Obesity")

if __name__ == "__main__":
    main()
