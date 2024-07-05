def defeats(n, e, powers, bonuses ):
    monsters = list(zip(powers, bonuses))
    monsters.sort(key = lambda x: x[0])
    defeated_count = 0
    for power, bonus in monsters:
        if e >= power:
            e += bonus
            defeated_count += 1
        else:
            break
        return defeated_count

n = int(input())
e = int(input())

powers = []
bonuses = []

for _ in range(n):
    powers.append(int(input()))

for _ in range(n):
    bonuses.append(int(input()))

# Output the result
print(defeats(n, e, powers, bonuses))