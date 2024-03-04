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
       
       newLevel.time = level["time"]
       newLevel.num_chips = level["num_chips"]
       newLevel.upper_layer = level["upper_layer"]
       newLevel.lower_layer = level["lower_layer"]
       newLevel.level_number=level["level_number"]
       newLevel.add_field(cc_classes.CCMapTitleField(level["title"]))
       intPassword=level["password"]
       listPassword = [int(str(intPassword)[i:i+3]) for i in range(0, len(str(intPassword)), 3)]
      
       newLevel.add_field(cc_classes.CCEncodedPasswordField(listPassword))
       newLevel.add_field(cc_classes.CCMapHintField(level["hintText"]))
       monsters=[]
       for monster in level["monsters"]:
          newmonstercoords=cc_classes.CCCoordinate(x=monster["x"],y=monster["y"])
          monsters.append(newmonstercoords)
       newLevel.add_field(cc_classes.CCMonsterMovementField(monsters))


       CCLevelPack.add_level(newLevel)
    return CCLevelPack





input_json_file = "test_map.json"



with open(input_json_file, "r") as reader:

    level_pack= json.load(reader)
 
    output=make_CCLevelPack(level_pack)

    print(output)
    dat_file = "/Users/emma/Documents/cmu sem4/programming for game designers/chips_tools/test_map.dat"
    cc_dat_utils.write_cc_level_pack_to_dat(output, dat_file)
    """Writes the given CC dat in binary form to the file
    Args:
        cc_dat (CCData): the cc data to write
        dat_file (string): the filename of the output file
    """


