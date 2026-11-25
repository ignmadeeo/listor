import data
import show
import random

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

temperatures = data.get_temperatures()
print("Antal temperaturer:", len(temperatures))
print("Högsta temperatur:", max(temperatures))
print("Lägsta temperatur:", min(temperatures))
average = sum(temperatures) / len(temperatures)
print("Medeltemperatur:", average)

for temperature in temperatures:
    if temperature > average:
        print(temperature)

scores = data.collect_scores()
print("Alla resultat:", scores)
print("Högsta resultat:", max(scores))
print("Lägsta resultat:", min(scores))
print("Medelvärde:", sum(scores) / len(scores))

temperatures = data.get_temperatures()
show.show_temperatures(temperatures)

events = data.get_events()
event = random.choice(events)
print("Händelse:", event)