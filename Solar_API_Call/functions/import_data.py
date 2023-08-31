import json
import os
import pandas as pd

def import_previous_api_call(cwd, src_params):

    # load a file if one does not exist
    try:
        # check if there is a file to read first - uses json_key
        filepath = os.path.join(cwd, "data_storage", f"{src_params['ProjRefID']}_storage.json")
        with open(filepath, "r") as openfile:
            # read the json file
            json_dict = json.load(openfile)
    except FileNotFoundError:
        return False

    json_object = json.dumps(json_dict, indent=4)

    return json_object


def import_weather_file(cwd):

    # TODO replace this with the file selector filepath in the interface
    filename = "sample_weather_data.csv"
    filepath = os.path.join(cwd, "inputs", filename)
    weather_file_df = pd.read_csv(filepath, header=2)

    return weather_file_df


def json_dumps(json_data, cwd):
    # create a custom key for it to identify files and API calls - uses json_key
    json_key = json_data['SystemAttributes']['ProjRefID']
    # function to dump json data
    json_object = json.dumps(json_data, indent=4)
    filepath = os.path.join(cwd, "data_storage", f"{json_key}_storage.json")
    with open(filepath, "w") as outfile:
        outfile.write(json_object)

    return
