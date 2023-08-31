import os
from inputs.params import src_energy_manual_args as src_params
from functions import api_call, import_data
import pandas as pd

def main(weather_file):
    """
    This project will call the SRC api for multiple configurations to run optimization efforts.
    It will also produce analysis, visuals and data outputs from the returns from the API
    :param name: SRC_Key - this is an enviromental variable in my configuration but users will need to supply either a
    team or individual key to use this project, can't store this on Github
    :return:
    Data visualizations
    Analysis information
    etc. (TBD)
    """

    cwd = os.getcwd()

    # api call url
    src_energy_manual_url = r'https://api.src.dnv.com/api/site/energy-manual'

    # TODO temp - get weatherfile imported for a single run
    # weather_df = import_data.import_weather_file(cwd)

    # get weather file from file selector on interface
    weather_df = pd.read_csv(weather_file)

    # call in stored data function
    # if there is already a datafile stored for this api run, pull it in here
    json_data = import_data.import_previous_api_call(cwd, src_params)
    if not json_data:
        # API Call if there is no json data file stored to run
        json_data = api_call.api_call_func(os.environ["API_KEY"], src_energy_manual_url, src_params, weather_df, 35, 1.25, 100000)
        # dump data to json to save on api calls
        import_data.json_dumps(json_data, cwd)

    return json_data



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
