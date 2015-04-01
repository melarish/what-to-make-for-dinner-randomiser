from random import randint

food_list = [
    "fried rice",
    "spanish omelette",
    "orange chicken & steamed veg",
    "pho",
    "bobotie http://www.facebook.com/l.php?u=http%3A%2F%2Fwww.bbcgoodfood.com%2Frecipes%2F5109%2Fbobotie&h=nAQEIxrse http://veggiebunch.co.za/vegan-lentil-bobotie-recipe/",
    "Chinese ribs",
    "paella http://www.veganuary.com/recipes/macro-paella/",
    "Indonesian noodles",
    "marinated red wine tofu http://www.platesforplants.com/blog/baked-tofu-with-red-wine-mushroom-sauce/",
    "chestnut and mushroom pie",
    "enchiladas/fajitas/something else Mexican",
    "satay noodles",
    "jamaican burgers",
    "butter bean artichoke pie http://veganrecipeclub.org.uk/vegetarian-vegan-recipe/artichoke-butterbean-filo-pie-olives-and-sundried-tomatoes",
    "dal",
    "thai curry",
    "cabbage stew",
    "potato and leek soup",
    "avocado pasta http://www.facebook.com/l.php?u=http%3A%2F%2Fdamndelicious.net%2F2014%2F06%2F20%2Favocado-pasta%2F&h=QAQEJPsDz",
    "cauliflower pizza http://deliciouslyella.com/vegan-pizza-gluten-dairy-yeast-free/",
    "spinach and cashew pasta",
    "crispy chili duck",
    "Indian curry",
    "cannelloni http://www.vegangela.com/2010/10/22/vegan-spinach-manicotti/",
    "chili http://vegan2014.motionlabclients.co.uk/31-day-menu/15",
    "African beans",
    "aubergine and tomato curry http://vegan2014.motionlabclients.co.uk/31-day-menu/13",
    "sausage n mash",
    "aubergine+artichoke pasta dish http://vegan2014.motionlabclients.co.uk/31-day-menu/8",
    "marinated tofu wraps http://vegan2014.motionlabclients.co.uk/31-day-menu/2",
    "vegan naan bread",
    "minestrone soup http://vegetarian.about.com/od/soupsstewsandchili/r/minestronesoup.htm",
    "fajita sauce wraps with black beans http://vegan2014.motionlabclients.co.uk/31-day-menu/1",
    "fake steak ale pie",
    "carrot&coriander soup http://serenitywomble.wordpress.com/2010/10/25/carrot-and-potato-soup-without-a-blender/ http://myveganfoodblog.wordpress.com/2013/02/10/simple-carrot-and-coriander-soup/",
    "walnut roast http://ohsheglows.com/2012/10/05/glazed-lentil-walnut-apple-loaf-revisited/",
    "tomato&pine risotto http://www.vegangela.com/2011/04/09/easy-baked-tomato-risotto/",
    "mushotto http://vegangela.com/2010/10/21/vegan-mushroom-risotto/",
    "lasagna",
    "sushi",
    "pasta salad",
    "quiche",
    "Italian salad",
    "Jamaican coconut sweet potato curry",
    "lentil stew http://www.bbc.co.uk/food/recipes/almond_lentil_stew_69086",
    "pizza"
]

def main():
    try_again = "y"
    while try_again == "y":
        food_id = randint(0, len(food_list)-1)
        food = food_list[food_id]
        del food_list[food_id]
        print("Why don't you make some %s" % food)
        try_again = raw_input("Or would you like something different? y/n")

    return


if __name__ == '__main__':
    main()