import random
import string

destinations_list = ['china', 'beijing', 'shanghai', 'shenzhen', 'dalian', 'hong kong', 
                     'japan', 'tokyo', 'osaka', 'korea', 'seoul', 'taiwan', 'taipei',
                     'central america', 'costa rica', 'spain', 'barcelona', 'madrid', 
                     'united states', 'los angeles', 'san diego','san francisco', 'seattle']

#list of responses, not good to separate
response_dict = {'china': ["Here are all the cities that I've traveled to in "\
                           "China if you would like to hear more: Beijing, Shanghai, Shenzhen, "\
                           "Dalian, Hong Kong"],
                'japan': ["Here are all the cities that I've traveled to in "\
                          "Japan if you would like to hear more: Tokyo, Osaka"],
                'korea': ["Here are all the cities that I've traveled to in "\
                          "Korea if you would like to hear more: Seoul"],
                'taiwan': ["Here are all the cities that I've traveled to in "\
                           "Taiwan if you would like to hear more: Taipei"],
                'spain': ["Here are all the cities that I've traveled to in "\
                          "Spain if you would like to hear more: Barcelona, Madrid"],
                'united states': ["Here are all the cities that I've traveled "\
                                  "to in the U.S. if you would like to hear more: Los Angeles, "\
                                  "San Diego, San Francisco, New York, Seattle"],
                'central america': ["Here are all the cities that I've traveled "\
                                    "to in Central America if you would like to hear more: Costa Rica"],
                'beijing': ["Beijing is China's capital city and is known "\
                            "for its rich cultural and historical landmarks. Definetly try out the "\
                            "small eats and Peking Duck if you're ever in Beijing!",
                            "For history and culture enthusiasts, make sure to visit "\
                            "Tiananmen Square, The Forbidden City, or The Great Wall of China!"],
                'shanghai': ["Shanghai is China's most westernized city and is a melting "\
                             "pot of culture and heritages. It has a mix of modern and "\
                             "historical influences and has amazing food from all over the world!",
                             "When in Shanghai, make sure to check out the Yu Garden, The Bund, and "\
                             "Nanjing Road for a unique cultural experience!"],
                'shenzhen': ["Shenzhen is one of China's most modern metropolis and "\
                             "is a bustling city full of hard working professionals and is China's "\
                             "gateway to Hong Kong.", "When in Shenzhen, make sure to visit Window "\
                             "of the World and Splendid China Folk Village to widen your world view!"],
                'dalian': ["Dalian is a modern port city that has many Russian and "\
                           "Japanese influences. It is a beautiful city to go to if you "\
                           "want to be near the beach!",
                           "When in Dalian, make sure to check out Dalian Forest Zoo or Xinghai Square!"],
                'hong kong': ["Hong Kong is a bustling city full of ambitious spirits "\
                              "and is a giant melting pot of culture from all around the world! "\
                              "Dim sum in HK is a must!",
                              "When in Hong Kong, make sure to also check out Macau if there's "\
                              "time and to visit Victoria Harbor and Ocean Park!"],
                'tokyo': ["Tokyo, Japan’s busy capital, mixes the ultramodern and the "\
                          "traditional, from neon-lit skyscrapers to historic temples.",
                          "Some popular attractions in Tokyo include: Tokyo Tower, Meiji Shrine, "\
                          "Shibuya Crossing, and Shinjuku."],
                'osaka': ["Osaka is a large port city and commercial center on the "\
                          "Japanese island of Honshu. It's known for its modern architecture, "\
                          "nightlife and hearty street food.", 
                          "When in Osaka, make sure to check out Osaka Castle and Dotonbori "\
                          "for a unique cultural experience!"],
                'seoul': ["Seoul is the capital of South Korea and is a huge "\
                          "metropolis where modern skyscrapers, high-tech subways and "\
                          "pop culture meet Buddhist temples, palaces and street markets.", 
                          "When in Seoul, make sure to check out Myeong-dong for shopping, "\
                          "N Seoul Tower for views, and Bukchon Hanok Village for the culture!"],
                'taipei': ["Taipei, the capital of Taiwan, is a modern metropolis "\
                           "with Japanese colonial lanes, busy shopping streets and contemporary buildings.",
                           "When in Taipei, make sure to check out Taipei 101, Shilin Night Market, and "\
                           "the bakeries."],
                'costa rica': ["Costa Rica is a rugged, rainforested Central "\
                               "American country with coastlines on the Caribbean and Pacific.", 
                               "Costa Rica is known for its beaches, volcanoes, and biodiversity. "\
                               "When there, make sure to check out Monteverde Cloud Forest Reserve, "\
                               "Arenal Volcano, and Parque Nacional Manuel Antonio."],
                'barcelona': ["Barcelona, the cosmopolitan capital of Spain’s Catalonia "\
                              "region, is known for its art and architecture.", 
                              "When in Barcelona, make sure to visit La Sagrada Familia, "\
                              "Park Güell, and Casa Milà."],
                'madrid': ["Madrid, Spain's central capital, is a city of elegant "\
                           "boulevards and expansive, manicured parks such as the Buen Retiro. "\
                           "It’s renowned for its rich repositories of European art.",
                           "When in Madrid, visit the Plaza Mayor, El Retiro Park, and the shopping plazas!"],
                'los angeles': ["Los Angeles has long been known as the city of Angels! "\
                                "There is a variety of activities to do in LA from hiking the "\
                                "Hollywood sign to chilling at Santa Monica beach or even shopping at Third Street!",
                                "When in LA, make sure to check out the art museums, modern cafes, and Hollywood "\
                                "night life!"],
                'san diego': ["San Diego truly embodies the California spirit, take a stroll "\
                              "through any of the fabulous beaches here or go paragliding at Torrey Pines on "\
                              "your day off!", "When in SD, make sure to check out Balboa Park for pretty "\
                              "botanical gardens, Little Italy for yummy Italian food, and San Diego Zoo "\
                              "for a fun time!"],
                'san francisco': ["A popular tourist destination, San Francisco is known "\
                                  "for its cool summers, fog, steep rolling hills, eclectic mix of architecture, "\
                                  "and landmarks, including the Golden Gate Bridge, cable cars, the former "\
                                  "Alcatraz Federal Penitentiary, Fisherman's Wharf, and its Chinatown district.", 
                                  "Make sure to check out the Japanese Friendship Garden, Golden Gate Bridge, "\
                                  "and SF's Chinatown!"],
                'seattle': ["Seattle is surrounded by water, mountains and evergreen forests, "\
                            "and contains thousands of acres of parkland.", 
                            "Washington State’s largest city, it’s home to a large tech industry, "\
                            "with Microsoft and Amazon headquartered in its metropolitan area. "\
                            "The futuristic Space Needle, a 1962 World’s Fair legacy, is its most iconic landmark."],
                }

food_dict = {'china': 'hot pot',
             'korea': 'korean barbeque',
             'japan': 'ramen and sushi',
             'taiwan': 'beef noodle soup and stinky tofu',
             'central america': 'corn',
             'united states': 'Burgers and pizza and vegan food',
             'spain': 'hot chocolate and churros',
             'beijing': 'peking duck',
             'shanghai': 'xiao long bao',
             'shenzhen': 'cantonese food',
             'dalian': 'seafood',
             'hong kong': 'dim sum',
             'tokyo': 'sushi',
             'osaka': 'street food in dotonbori',
             'seoul': 'street food in myeongdong',
             'taipei': 'little sausage in big sausage',
             'costa rica': 'gallo pinto',
             'barcelona': 'paella',
             'madrid': 'Cocido Madrileñ',
             'los angeles': 'anything',
             'san diego': 'mexican food',
             'san francisco': 'seafood',
             'seattle': 'seafood',
            }

#responses to other inputs
invalid_list = ['Sorry, I do not know much about that location. Please try a different location. Maybe these countries: China, Taiwan, Japan, Korea, United States, Central America, or Spain.',
                'Not a valid location. Sorry, can we talk about a different location?',
                'Let us try talking about somewhere else!']

#Code from A3
def remove_punctuation(input_string):
    out_string = ""
    for item in input_string:
        if item not in string.punctuation:
            out_string += item
    #print(out_string)
    return out_string

def prepare_text(input_string):
    input_string = input_string.lower()
    input_string = remove_punctuation(input_string)
    out_list = input_string.split()
    return out_list

def selector(input_list, check_list, return_list):
    output = None
    for item in input_list:
        if item in check_list:
            output = random.choice(return_list)
            break 
    return output

def string_concatenator(string1, string2, separator):
    return string1 + separator + string2

def list_to_string(input_list, separator):
    output = input_list[0]
    for item in input_list[1:]:
        output = string_concatenator(output, item, separator)
    print(output)
    return output

def end_chat(input_list):
    return 'quit' in input_list

def is_in_list(list_one, list_two):
    """Check if any element of list_one is in list_two."""   
    for element in list_one:
        if element in list_two:
            return True
    return False

def find_in_list(list_one, list_two):
    """Find and return an element from list_one that is in list_two, or None otherwise."""
    for element in list_one:
        if element in list_two:
            return element
    return None

#Search for locations and user input
def find_topic(userinput):
    message = userinput.lower()
    found = False
    #loop through destinations list and print random response if it is found
    for place in destinations_list:
        if place in message:
            print(response_dict[place][random.randint(0, len(response_dict[place]))-1])
            find_food(place)
            found = True
    #if no location found, print error message
    if not found:       
        print(invalid_list[random.randint(0, len(invalid_list)-1)])
    else: 
        print("What other location do you want to hear more about?")
    return

#continuously parse user input for location until terminated
def travel_bot():
    print("Hi! I'm Kio, I'm here to help you with your travel journeys! What location would you like to know more about?\n")
    #infinite loop until user breaks it
    while True:
        #getting input from user
        msg = input()
        #check if message is quit
        if msg == 'quit':
            print('Thanks so much for chatting with me! Have a nice trip!')
            break
        #otherwise search for locations and re-prompt
        find_topic(msg)
        
#finding foods in the given place        
def find_food(place):
    print("Some foods to try here are: " + food_dict[place])
