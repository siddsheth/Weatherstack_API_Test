# WeatherStack API

An API Testing project which tests WeatherStack's Current Weather APIs with different units and Location identifiers.

**Test Cases**

| Test Description | Resource | Query Parameters | Test Data | Expected Results | Validation Details|
| --- | --- | --- | --- | --- | --- |
| Get Current weather data for a specified Location | current | {Valid API Key} + City Name | Query = London | API should return current weather data of the location given. | Status Code is verified to check API response. Request details to verify that correct request is submitted to server. Location details to verify correct detail received in response. |
| Get Current weather data for a specified Location in specified unit | current | {Valid API Key} + City Name + Unit | Query = London, Unit = f | API should return current weather data of the given location in given unit. | Status Code is verified to check API response. Request details to verify that correct request and unit is submitted to server. Location details to verify correct detail received in response. |
|Get Current weather data for a specified Zipcode | Current |{Valid API Key} + Zipcode | Query = 60018 | API should return current weather data of the given zipcode | Status Code is verified to check API response. Request details to verify that correct request and location identifier is submitted to server. Location details to verify correct detail received in response. |
| Get Current weather data for a specified Latitude and Longitude. | current | {Valid API Key} + Lat, Long | Query = 40.728,-74.078 | API should return current weather data of the given Lat Long | Status Code is verified to check API response. Request details to verify that correct request and location identifier is submitted to server. Location details to verify correct detail received in response. Also verify Latitude Longitude is correct|
| Try to get current weather data with invalid API Key | current | {Invalid API Key} + City Name | {Invalid API Key} + Query = London | API Should return Invalid API Key message in response | Verified the entire response |
| Try to get current weather data without providing any API Key | current | {No API Key} + City Name | {No API Key} + Query = London | API Should return Missing API Key message in response | Verified the entire response |


## Demo

![GIF](https://github.com/siddsheth/Weatherstack_API_Test/blob/main/Weatherstack_API_Test.gif)



## Authors

- [@siddsheth](https://github.com/siddsheth)
