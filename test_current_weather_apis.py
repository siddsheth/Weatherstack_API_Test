import time
import requests
import pytest
from utilities.configurations import getConfig
from utilities.resources import ApiResources

config = getConfig()
endpoint = config["API"]["endpoint"] + ApiResources.current
api_key = "278ca3f65a3cf690516645d301007c1a"

only_location_params = {"access_key": api_key,  "query": "London"}
location_with_unit_params = {"access_key": api_key, "query": "London", "units": "f"}
location_with_zipcode_params = {"access_key": api_key, "query": "60018"}
location_with_lat_long_params = {"access_key": api_key, "query": "40.728,-74.078"}
invalid_api_key_params = {"access_key": "278ca3f65a", "query": "Paris"}
missing_api_key_params = {"query": "Tokyo"}

only_location_validation = {"type": "City", "query": "London, United Kingdom", "language": "en", "unit": "m", "name": "London", "country": "United Kingdom", "region": "City of London, Greater London", "timezone_id": "Europe/London"}
location_unit_validation = {"type": "City", "query": "London, United Kingdom", "language": "en", "unit": "f", "name": "London", "country": "United Kingdom", "region": "City of London, Greater London", "timezone_id": "Europe/London"}
location_zip__validation = {"type": "Zipcode", "query": "60018", "language": "en", "unit": "m", "name": "Des Plaines", "country": "USA", "region": "Illinois", "timezone_id": "America/Chicago"}
location_latlong_validation = {"type": "LatLon", "query": "Lat 40.73 and Lon -74.08", "language": "en", "unit": "m", "name": "Jersey City", "country": "United States of America", "region": "New Jersey", "lat": "40.728", "lon": "-74.078", "timezone_id": "America/New_York"}
invalid_api_key_validation = {"success": False, "error": {"code": 101, "type": "invalid_access_key", "info": "You have not supplied a valid API Access Key. [Technical Support: support@apilayer.com]"}}
missing_api_key_validation = {"success": False, "error": {"code": 101, "type": "missing_access_key", "info": "You have not supplied an API Access Key. [Required format: access_key=YOUR_ACCESS_KEY]"}}


@pytest.mark.parametrize("inputs", [(only_location_params, only_location_validation), (location_with_unit_params, location_unit_validation), (location_with_zipcode_params, location_zip__validation), (location_with_lat_long_params, location_latlong_validation)])
def test_current_weather_api_test(inputs):

    response = requests.get(endpoint, params=inputs[0])
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; Charset=UTF-8"

    response_json = response.json()
    assert inputs[1]["type"] == response_json["request"]["type"]
    assert inputs[1]["query"] == response_json["request"]["query"]
    assert inputs[1]["language"] == response_json["request"]["language"]
    assert inputs[1]["unit"] == response_json["request"]["unit"]
    assert inputs[1]["name"] == response_json["location"]["name"]
    assert inputs[1]["country"] == response_json["location"]["country"]
    assert inputs[1]["region"] == response_json["location"]["region"]
    assert inputs[1]["timezone_id"] == response_json["location"]["timezone_id"]

    if inputs[1]["type"] == "LatLon":
        assert inputs[1]["lat"] == response_json["location"]["lat"]
        assert inputs[1]["lon"] == response_json["location"]["lon"]

    # Adding this delay since getting status code 429-too_many_requests while executing this script
    time.sleep(3)


@pytest.mark.parametrize("inputs", [(invalid_api_key_params, invalid_api_key_validation), (missing_api_key_params, missing_api_key_validation)])
def test_current_weather_api_negative_tests(inputs):
    response = requests.get(endpoint, params=inputs[0])
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; Charset=UTF-8"

    response_json = response.json()
    assert inputs[1] == response_json

    # Adding this delay since getting status code 429-too_many_requests while executing this script
    time.sleep(3)
