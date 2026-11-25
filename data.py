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

def get_scores():
    scores = [20, 45, 60, 30, 80, 55, 90, 40]
    return scores

def get_temperatures():
    temperatures = [12, 15, 18, 14, 11, 20, 16]
    return temperatures