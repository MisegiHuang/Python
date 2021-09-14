import random
yut_points = [0]
yut_each = [0, 0, 0, 0]
yut_credits = 0
for i in yut_points:
    input("윷을 던지겠습니다. Enter 키를 눌러 주세요.")
    yut_seq = 0
    for j in yut_each:
        random.seed()
        yut_benchmark = random.randrange(40, 51)
        yut_result = random.randrange(0, 100)
        if yut_result >= yut_benchmark:
            print((yut_seq + 1), "번째 윷: 배")
            yut_each[yut_seq] = 1
            yut_points[yut_credits] += 1
        else:
            print((yut_seq + 1), "번째 윷: 등")
        yut_seq += 1
    print(yut_each)
    if yut_points[yut_credits] == 0:
        yut_points[yut_credits] = 5
        print((yut_credits + 1), "번째로 던져 나온 끗은 >모<입니다.")
    if yut_points[yut_credits] == 1:
        if yut_each[3] == 1:
            yut_points[yut_credits] = -1
            print((yut_credits + 1), "번째로 던져 나온 끗은 >뒷도<입니다.")
        else:
            print((yut_credits + 1), "번째로 던져 나온 끗은 >도<입니다.")
    if yut_points[yut_credits] == 2:
        print((yut_credits + 1), "번째로 던져 나온 끗은 >개<입니다.")
    elif yut_points[yut_credits] == 3:
        print((yut_credits + 1), "번째로 던져 나온 끗은 >걸<입니다.")
    elif yut_points[yut_credits] == 4:
        print((yut_credits + 1), "번째로 던져 나온 끗은 >윷<입니다.")
    if yut_points[yut_credits] >= 4:
        print("윷이나 모가 나왔어요! 한 번 더 던집시다.")
        yut_points.append(0)
        yut_credits += 1
        yut_each = [0, 0, 0, 0]
yut_credits = 0
print(len(yut_points), "번 윷을 던져서 나온 끗은 다음과 같습니다.")
for k in yut_points:
    print((yut_credits + 1), "번째 끗은", yut_points[yut_credits], "입니다.")
    yut_credits += 1
input("계속하려면 Enter 키를 눌러 주세요.")
