import json

def convert_for_sj(data, location):
    entry = {}

    for i in data["titles"]:
        x = {"position" : data["titles"][i], "company" : data["companies"][i], "jobLink" : data["links"][i], "date_posted" : data["date_listed"][i], "location" : location, "description" : data["summary"][i], "categories" : (), "skills" : ()}
        # x = (data["titles"][i], data["companies"][i], data["links"][i])
        entry[i] = x

        for z in entry[i]["position"]:
            x = "\nnew"
            y =entry[i]["position"]
            if x in y:
                new_string = y.replace(x,"")
                entry[i]["position"] = new_string
                print(new_string)

            bad = "\n"
            state = entry[i]["description"]
            if bad in state:
                new_string_2 = state.replace(bad,"")
                entry[i]["description"] = new_string_2
                print(new_string_2)

    json_object = json.dumps(entry)

    with open("converted_data.json", 'w') as k:
        data_dump = json.dump(entry, k)

    print("Conversion complete!")

##############
with open("scraped_data.json") as f:
    data = json.load(f)

convert_for_sj(data, "San Francisco Bay Area")
