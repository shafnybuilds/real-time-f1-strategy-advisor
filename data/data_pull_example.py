import fastf1 as ff
import os


def get_driver_data(year, gp, mod, driver_code):

    # i had some issues with caching when i try to import this func to my notebook -> so i'm creating a abs cache dir here
    current_dir = os.path.dirname(os.path.abspath(__file__))
    cache_dir = os.path.join(current_dir, "cache")

    # create cache dir if it doesn't exist
    if not os.path.exists(cache_dir):
        os.mkdir(cache_dir)

    ff.Cache.enable_cache(cache_dir)

    session = ff.get_session(year, gp, mod)

    session.load(telemetry=False, laps=False, weather=False)

    driver = session.get_driver(driver_code)

    return driver


# sample calling of get_driver_data func
max = get_driver_data(2022, "Bahrain", "R", "VER")
print(max)
