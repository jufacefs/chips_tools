import cc_dat_utils
import cc_classes


import json

#Part 3
#Load your custom JSON file
#Convert JSON data to CCLevelPack
#Save converted data to DAT file





def make_CCLevelPack(level_pack):

    CCLevelPack= cc_classes.CCLevelPack()

    levels=level_pack['levels']
    for level in levels:
       newLevel=cc_classes.CCLevel()
       newLevel.level_number = level["level_number"]
       newLevel.time = level["time"]
       newLevel.num_chips = level["num_chips"]
       newLevel.upper_layer = level["upper_layer"]
       newLevel.lower_layer = level["lower_layer"]

       newLevel.add_field(cc_classes.CCMapTitleField(level["fields"]["3"]))
       newLevel.add_field(cc_classes.CCEncodedPasswordField(level["fields"]["6"]))
       newLevel.add_field(cc_classes.CCMapHintField(level["fields"]["7"]))
       monsters=[]
       for monster in level["fields"]["10"]:
          newmonstercoords=cc_classes.CCCoordinate(x=monster["x"],y=monster["y"])
          monsters.append(newmonstercoords)
       newLevel.add_field(cc_classes.CCMonsterMovementField(monsters))


    #    newLevel=level_pack.CCLevel(level_number = level["level_number"],
    #                                time = level["time"],
    #                                num_chips = level["num_chips"],
    #                                upper_layer = level["upper_layer"],
    #                                lower_layer = level["lower_layer"],
    #                                optional_fields = fields)

        #Create a new Game object from the json_data by reading
        # platform=test_data.Platform(launch_year=game["platform"]["launchyear"],
        #                             name=game["platform"]["name"])
        # newGame=test_data.Game(title=game["title"],platform=platform,year=game['Year'])
       CCLevelPack.add_level(newLevel)


    return CCLevelPack



#Part 2
input_json_file = "level_pack.json"

### Begin Add Code Here ###

with open(input_json_file, "r") as reader:
    #Use the json module to load the data from the file
    level_pack= json.load(reader)
 
    output=make_CCLevelPack(level_pack)

    # print(output)
    dat_file = "/Users/emma/Documents/cmu sem4/programming for game designers/chips_tools/jiumanz_cc1.dat"
    cc_dat_utils.write_cc_level_pack_to_dat(output, dat_file)
    """Writes the given CC dat in binary form to the file
    Args:
        cc_dat (CCData): the cc data to write
        dat_file (string): the filename of the output file
    """


### End Add Code Here ###