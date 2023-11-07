import json
import math

def main():

    STAT_ARRAY = "Param_39_26ADF7E94CDC32CEEDEF2CA219E264BF"

    STAT_MAPPINGS = {
        "HP":"HP_38_60C1981648472447396094AC51E6861E",
        "MP":"MP_39_F930AFBC4A48BE8BF00009B7841D66D5",
        "BP":"BP_36_2C9BF89744A5CC49B1ABF09F3658810E",
        "SHLDS":"SP_37_35AF0F444214CE52D722FE9785D9DEA5",
        "ATK":"ATK_40_4AB44CD740D8A6BF06E3A0A6B62FF589",
        "DEF":"DEF_41_BAE3A0D84D0AD654D3F0D68D467163E3",
        "MATK":"MATK_42_6CE7342144ABD5515E1DCFB07DB6F9EA",
        "MDEF":"MDEF_43_F437EF5F447142384DD0BA91294B3A3B",
        "ACC":"ACC_44_C4B000CE4B3238F27EC316896A346DB8",
        "EVA":"EVA_45_D1A7250742962DB6306A7295D71AADE7",
        "CRIT":"CON_46_9BCE805749432E94492E49B0EE90D7FF",
        "SPD":"AGI_47_2F9420C345AFAAE3A5D6CC9F78B42D5D"
    }

    STAT_SCALARS = {
        "HP":1.35,
        "SHLDS":1.5,
        "OTHERS":1.25
    }

    # open
    with open("Base\Octopath_Traveler\Content\Character\Database\EnemyDB.json", "r") as file:
        big_json = json.load(file)

    # do modification
    # print(data)

    for monster in big_json['Exports'][0]['Table']['Data']:
        for item in monster['Value']:
            if 'Name' in item and item['Name'] == STAT_ARRAY:
                # Access the dictionary with the desired "Name" value
                # print(item["Value"])
                for stat in item['Value']:
                    # print(stat["Name"])
                    # print(f"old stat: {stat['Value']}")
                    
                    if stat["Name"] == STAT_MAPPINGS["HP"]:
                        scalar = STAT_SCALARS["HP"]
                    elif stat["Name"] == STAT_MAPPINGS["SHLDS"]:
                        scalar = STAT_SCALARS["SHLDS"]
                    else:
                        scalar = STAT_SCALARS["OTHERS"]
                    # print(f"Scalar to multiply by is {scalar}")

                    stat["Value"] = math.floor(stat["Value"] * scalar)
                    # print(f"new stat: {stat['Value']}")
                # exit()
                    
                
    with open('EnembyDB.json', 'w') as file:
        json.dump(big_json, file, indent=2)

    return 0

if __name__ == "__main__":
    main()