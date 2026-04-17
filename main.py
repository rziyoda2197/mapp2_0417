# 1. Kvadrat
print("1. Kvadrat:", list(map(lambda x: x**2, [1,2,3,4,5])))

# 2. Katta harf
print("2. Katta harf:", list(map(str.upper, ["salom", "dunyo"])))

# 3. Ikki baravar
print("3. Ikki baravar:", list(map(lambda x: x*2, [5,10,15])))

# 4. Uzunlik
print("4. Uzunlik:", list(map(len, ["salom", "python", "map"])))

# 5. Yig'indi
print("5. Yig'indi:", list(map(lambda x,y: x+y, [1,2,3], [10,20,30])))

# 6. Absolyut
print("6. Absolyut:", list(map(abs, [-7, 4, -12])))

# 7. Teskari
print("7. Teskari:", list(map(lambda s: s[::-1], ["salom", "python"])))
