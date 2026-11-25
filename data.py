def get_film():
    film = ["flash", "spiderman", "batman", "uncharted", "Lupin"]
    return film

def get_spel():
    spel = ["minecraft", "brawlstar","gta 6", "roblox","fortnite"]
    return spel


def get_shopping_list():
    shopping_list = [" salt godis","choklad", "chips"]

    shopping_list.append("lakris")
    shopping_list.append( "sura godisar")

    shopping_list.insert(1,"söta godisar")

    shopping_list.remove( " salt godis")

    removed_item = shopping_list.pop(2)

    print("Borttagen vara:",removed_item)

    return shopping_list

print(get_shopping_list())