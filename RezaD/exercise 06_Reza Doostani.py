import random

level = int(input("Enter level 1 or 2 or 3: "))
if level == 1:
    low_limit = 1
    heigh_limit = 10

elif level == 2:
    low_limit = 11
    heigh_limit = 99

elif level == 3:
    low_limit = 100
    heigh_limit = 999

operator = "+"

rights = wrongs = wrongs_time = 0

for i in range(5):
    first_operand = random.randint(low_limit, heigh_limit)
    seccond_operand = random.randint(low_limit, heigh_limit)
    result = first_operand + seccond_operand

    question = " ".join([str(first_operand), operator, str(seccond_operand), "= "])
    answer = input(question)

    if int(answer) == result:
        rights += 1
        continue
    
    elif int(answer) != result and wrongs_time <= 2:
        while wrongs_time <= 2 and int(answer) != result:
            answer = input(question)
            if int(answer) != result:
                wrongs_time += 1
            elif int(answer) == result:
                rights += 1
            if wrongs_time == 2:
                wrongs += 1
                print(result)
                wrongs_time = 0
                break

score = str(rights) + " right, " + str(wrongs) + " wrong."
print("\nYour score:", score)
