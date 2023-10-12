while True:
    try:
        import random

        # Imports the random library

        print()
        quiz_level = int(input("Enter the level of quiz (1, 2, 3): "))
        # Gets an input of the quiz level

        if quiz_level == 1:
            quiz_max_number = 10

        elif quiz_level == 2:
            quiz_max_number = 100

        elif quiz_level == 3:
            quiz_max_number = 1000

        # Conditions for the quiz level and the max of number

        operator_list = ["+", "-", "*", "/"]
        # A list of operators

        final_score = 10

        for i in "ABCDEFGHIJ":
            first_number = random.randint(-(quiz_max_number - 1), quiz_max_number - 1)
            seccond_number = random.randint(-(quiz_max_number - 1), quiz_max_number - 1)
            operator = random.choice(operator_list)

            while (
                operator == "/"
                and round(first_number / seccond_number, 1)
                != first_number / seccond_number
                or seccond_number == 0
            ):
                first_number = random.randint(
                    -(quiz_max_number - 1), quiz_max_number - 1
                )
                seccond_number = random.randint(
                    -(quiz_max_number - 1), quiz_max_number - 1
                )

            print()
            quiz_pherase = input(f"{i}) {first_number} {operator} {seccond_number} = ")

            if "." in quiz_pherase:
                quiz_pherase = float(quiz_pherase)

            elif "." not in quiz_pherase:
                quiz_pherase = int(quiz_pherase)

            if operator == "+":
                quiz_answer = first_number + seccond_number

            elif operator == "-":
                quiz_answer = first_number - seccond_number

            elif operator == "/":
                quiz_answer = first_number / seccond_number

            elif operator == "*":
                quiz_answer = first_number * seccond_number

            if quiz_pherase == quiz_answer:
                print("Correct!")

            elif quiz_pherase != quiz_answer:
                print("Incorrect.")

                for j in range(2):
                    print()
                    quiz_pherase = input(
                        f"{i}) {first_number} {operator} {seccond_number} = "
                    )

                    if "." in quiz_pherase:
                        quiz_pherase = float(quiz_pherase)

                    elif "." not in quiz_pherase:
                        quiz_pherase = int(quiz_pherase)

                    if quiz_pherase == quiz_answer:
                        print("Correct!")
                        break

                    elif quiz_pherase != quiz_answer:
                        print("Incorrect.")

                if quiz_pherase != quiz_answer:
                    print(f"The correct answer is: {quiz_answer}")
                    final_score -= final_score
        if quiz_level == 10:
            quiz_level = 1

        elif quiz_level == 100:
            quiz_level = 2

        elif quiz_level == 1000:
            quiz_level = 3

        print()
        print(f"Your final score in level #{quiz_level} is: {final_score} of 10")
        print()

        if final_score < 2:
            print("Realy terrible. Try to be better.")

        elif 2 < final_score < 5:
            print("That was not good, try more.")

        elif 5 > final_score < 7:
            print("Good, but can be a lot better.")

        elif 7 > final_score < 10:
            print("Realy good! But you could be a little bit better.")

        elif final_score == 10:
            print("Great! You are the best!")

        print("Good luck!")
        print()

        break

    except:
        print("__________________________________________________________")
        print("Sorry, there is a problem and we should reset the program.")
        print("__________________________________________________________")
