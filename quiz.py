print("Welcome to the one piece quiz!")
print("You will have 5 questions relating to the popular anime/manga.")
score = 0

answered = 0

while answered <= 5:
    print("Question 1: What is the name of the location Sanji worked before joining the straw hats? ")
    print("A: Thriller Bark")
    print("B: Zou")
    print("C: Baratie")
    print("D: Fishman Island")
    answer1 = input()
    answered =+ 1
    if answer1.lower() == "c":
        score += 1
    else:
        score += 0
    print("Question 2: Who sacrificed himself in Impel Down? ")
    print("A: Bon Clay")
    print("B: Mihawk")
    print("C: Rob Lucci")
    print("D: Nico Robin")
    answer2 = input()
    answered =+ 1
    if answer2.lower() == "a":
        score += 1
    else:
        score += 0
    print("Question 3: Where is the first poneglyph read by Robin located? ")
    print("A: Alabasta")
    print("B: Whole Cake Island")
    print("C: Thriller Bark")
    print("D: Punk Hazard")
    answer3 = input()
    answered =+ 1
    if answer3.lower() == "a":
        score += 1
    else:
        score += 0    
    print("Question 4: What group is Bartholomew Kuma secretly apart of? ")
    print("A: The Marines")
    print("B: Revolutionary Army")
    print("C: Baroque Works")
    print("D: Germa 66")
    answer4 = input()
    answered =+ 1
    if answer4.lower() == "b":
        score += 1
    else:
        score += 0
    print("True or False: Corazon was retrieving a devil fruit with law for Doffy, not to save Law.")
    print("True")
    print("False")
    answered =+ 1
    answer5 = input()
    if answer5.lower() == "false":
        score += 1
        break
    else:
        score += 0
        break

if score >= 4:
    print(f"Congrats! You passed with {score} questions right!")
elif score == 0:
    print("You got them all wrong.")
else:
    print(f"Oh no! You only got {score} right. Better luck next time.")