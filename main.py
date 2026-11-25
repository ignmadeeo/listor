import data

filmer = data.get_film()
for film in filmer:
    if len(film) > 5:
        print(film)

scores = data.get_scores()
for score in scores:
    print(score)
for score in scores:
    print(score * 2)
for score in scores:
    if score > 50:
        print(score)

print(len(scores))
print(sum(scores))
print(min(scores))
print(max(scores))

values = [12, 18, 9, 24, 15]

sorted_values = sorted(values)

print("Sorterad lista:", sorted_values)
print("Ursprunglig lista:", values)

print(data.get_spel())
print(data.get_godis())