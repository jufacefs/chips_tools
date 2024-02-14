import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    ### Begin Add Code Here ###
    #Loop through the json_data
    games=json_data['Games']
    for game in games:
      

        #Create a new Game object from the json_data by reading
        platform=test_data.Platform(launch_year=game["platform"]["launchyear"],
                                    name=game["platform"]["name"])
        newGame=test_data.Game(title=game["title"],platform=platform,year=game['Year'])
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
        game_library.add_game(newGame)
    ### End Add Code Here ###

    return game_library



#Part 2
input_json_file = "test_data.json"

### Begin Add Code Here ###

with open(input_json_file, "r") as reader:
    #Use the json module to load the data from the file
    gameData = json.load(reader)
    #Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
    output=make_game_library_from_json( gameData )
    #Print out the resulting GameLibrary data using print()
    print(output)


### End Add Code Here ###










