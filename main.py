# 1
sonlar = [2, 3, 6, 9, 12, 15, 4, 7, 18, 5]

natija = list(filter(lambda x: x % 3 == 0 and x > 5, sonlar))
print(natija)

# 2
sozlar = ["radar", "salom", "level", "madam", "kitob", "noon"]

natija = list(filter(lambda s: s == s[::-1], sozlar))
print(natija)

# 3
royxat = [10, 20, 30, 40, 50, 60, 70]

natija = list(filter(lambda x: royxat.index(x) % 2 == 1, royxat))
print(natija)

# 4
sozlar = ["Salom", "hello", "Python", "world", "Apple", "banana"]

natija = list(filter(lambda s: s[0].isupper(), sozlar))
print(natija)

# 5
sonlar = [-5, -2, -1, 0, 1, 3, 4, 7, 9]

natija = list(filter(lambda x: x > 0 and x % 2 != 0, sonlar))
print(natija)

