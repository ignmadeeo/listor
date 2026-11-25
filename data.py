def get_film():
    film = ["flash", "spiderman", "batman", "uncharted", "Lupin"]
    return film

def get_spel():
    spel = ["minecraft", "brawlstar","gta 6", "roblox","fortnite"]
    return spel


def get_godis():
    godis = [" salt godis","choklad", "chips"]

    godis.append("lakris")
    godis.append( "sura godisar")

    godis.insert(1,"söta godisar")

    godis.remove( " salt godis")

    removed_item = godis.pop(2)

    print("Borttagen vara:",removed_item)

    return godis

print(get_godis())
print(get_film())
print(get_spel())