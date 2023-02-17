name = input("Welcome to GC mini golf! What is your name? ")
course_holes = input(f"Hello {name}! Would you like to play 3 or 6 holes? ")
if course_holes == "3":
    hole_one = input("How many putts for Hole 1? (par: 3) ")
    hole_two = input("How many putts for Hole 2? (par: 3) ")
    hole_three = input("How many putts for Hole 3? (par: 3) ")
    three_score = int(hole_one) + int(hole_two) + int(hole_three)
    three_par = 9
    three_total = three_score - three_par
    if three_score > 9:
        print(f"Nice try, {name}... Your total score was: +{three_total}.")
    if three_score < 9:
        print(f"Great job, {name}! Your total score was: {three_total}.")
    if three_score == 9:
        print(f"Good game, {name}. Your total score was: 0.")
elif course_holes == "6":
    hole_one = input("How many putts for Hole 1? (par: 3) ")
    hole_two = input("How many putts for Hole 2? (par: 3) ")
    hole_three = input("How many putts for Hole 3? (par: 3) ")
    hole_four = input("How many putts for Hole 4? (par: 3) ")
    hole_five = input("How many putts for Hole 5? (par: 3) ")
    hole_six = input("How many putts for Hole 6? (par: 3) ")
    six_score = int(hole_one) + int(hole_two) + int(hole_three) + int(hole_four) + int(hole_five) + int(hole_six)
    six_par = 18
    six_total = six_score - six_par
    if six_score > six_par:
        print(f"Nice try, {name}... Your total score was: +{six_total}.")
    if six_score < six_par:
        print(f"Great job, {name}! Your total score was: {six_total}.")
    if six_score == 18:
        print(f"Good game, {name}. Your total score was: 0.")
else:
    print("Invalid Answer")














