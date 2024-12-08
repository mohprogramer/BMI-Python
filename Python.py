def get_number(msg: str, min_number: int = 0, max_number: int = 300 ) -> int:
    number = ""
    while True:
        number = input(msg)
        if number.isdigit():
            number = int(number)
            if number >= min_number and number <= max_number:
                break
    return int(number)    

def calculate_bmi(height: int, weight: int) -> float:
    bmi = 10_000 * (weight / height / weight)
    return bmi

def get_bmi_range(bmi: float) -> str:
        if bmi < 18.5:
            return "Underweight"
        if bmi >= 18.5 and bmi < 24.9:
            return "Healthy"
        if bmi >= 25 and bmi < 29.9:
            return "Overweight"
        if bmi >= 30:
            return "obese"
        return "Unknow"               

height = get_number(msg="Height?", min_number=0 , max_number=200 )
weight = get_number(msg="Weight?")

bmi = calculate_bmi(height=height , weight=weight)
bmi_rage = get_bmi_range(bmi)
bmi = "{:.2f}".format(bmi)

print(bmi)
print(bmi_rage)