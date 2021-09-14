import random # To load the random module.
yut_points = [0] # Default results to archive at each chance; While the result is 'Yut' or 'Mo', player gets extra chance to throw.
yut_each = [0, 0, 0, 0] # Default results of each turning yut; It is always 4 yuts required to the game
yut_credits = 0 # The quantity of chance to throw
for i in yut_points: # The sequence of throwing yuts
    input("To throw yuts, press Enter key.") # To show the sense of throwing yuts
    yut_seq = 0 # To count each yut
    for j in yut_each: # To turn each yut to head or tail
        random.seed()
        """
        The probability of turning yuts is not fixed. Head side has it about 52% to 60%(reference from Korean Wikipedia '윷놀이').
        """
        yut_benchmark = random.randrange(40, 51) # Picking random number of benchmark.
        yut_result = random.randrange(0, 100) # Checking if this random number is more than the benchmark or not
        if yut_result >= yut_benchmark: # (the benchmark number to 99)
            print("No.", (yut_seq + 1), "Yut: Head")
            yut_each[yut_seq] = 1 # Turning to head from tail
            yut_points[yut_credits] += 1 # Raising up the point as each yut turns head side
        else: # (0 to the benchmark-1)
            print("No.", (yut_seq + 1), "Yut: Tail") # Neither turning yut side nor raising up the point occurs.
        yut_seq += 1 # Going to next yut
    print(yut_each) # Showing the result of all yuts
    if yut_points[yut_credits] == 0: # Every yuts are tail side
        yut_points[yut_credits] = 5 # Making the point 5
        print("Your point is >Mo< at the chance No.", (yut_credits + 1), ".") # Mo == 5 points
    if yut_points[yut_credits] == 1: # Only 1 yut is head side
        if yut_each[3] == 1: # The last yut for going backward
            yut_points[yut_credits] = -1 # Making the point 1 to backward(minus)
            print("Your point is >Do to backward< at the chance No.", (yut_credits + 1), ".") # Do == 1 point. In this case, to backward
        else: # The only head side yut is not the last
            print("Your point is >Do< at the chance No.", (yut_credits + 1), ".") # Do == 1 point. (Normal case)
    if yut_points[yut_credits] == 2:
        print("Your point is >Gae< at the chance No.", (yut_credits + 1), ".") # Gae == 2 points
    elif yut_points[yut_credits] == 3:
        print("Your point is >Geol< at the chance No.", (yut_credits + 1), ".") # Geol == 3 points
    elif yut_points[yut_credits] == 4:
        print("Your point is >Yut< at the chance No.", (yut_credits + 1), ".") # Yut == 4 points
    if yut_points[yut_credits] >= 4: # Extra chance to throw yuts once again if former result is 'Yut' or 'Mo'
        print("You got 'Yut' or 'Mo'! Let's throw again.")
        yut_points.append(0) # Adding the record of the new chance
        yut_credits += 1 # Running the loop once more
        yut_each = [0, 0, 0, 0] # Returning the yuts to default
yut_credits = 0 # The score of yut_credits got same with the length of yut_points. Therefore, yut_credits returns to default for next loop and the loop quotes the length instead of the credit point.
print("You threw yuts", len(yut_points), "time(s) and we show each reslut(s).")
for k in yut_points: # The loop to show each points of chance
    print("You got", yut_points[yut_credits], "point(s) at the No.", (yut_credits + 1), "chance.", )
    yut_credits += 1
input("Press Enter key to continue.") # To pause to check all running flow without at the command prompt
