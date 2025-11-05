# cities_obj = open("cities.txt", "w")                                
# cities_obj.write("Hyderabad\nDelhi\nMumbai\nChennai\nKolkata")       # It creates the file if the file doesn't exists and writes the content to the file.
# cities_obj.close()


### Over riding
cities_obj = open("cities.txt", "w")
cities_obj.write("Hyderabad\nDelhi\nMumbai\nChennai\nKolkata\nNagpur")        #The moment we open this file in write mode, it wipes the existing data and replaces with the new content given here.
cities_obj.close()