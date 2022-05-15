from django.shortcuts import render


def home(request):
    import json
    import requests

    if request.method == "POST":
        location = request.POST['location']
        api_request = requests.get("http://api.weatherapi.com/v1/current.json?key=078d7a99f6a54328abb71558221505&q"
                                   "=" + location + "&aqi=yes")
        try:
            api = json.loads(api_request.content)
            api['current']['air_quality']['us_epa_index'] = api['current']['air_quality']['us-epa-index']
            del api['current']['air_quality']['us-epa-index']

            api['current']['air_quality']['gb_defra_index'] = api['current']['air_quality']['gb-defra-index']
            del api['current']['air_quality']['gb-defra-index']

        except Exception as e:
            api = "Error..."

        if api['current']['air_quality']['us_epa_index'] == 1:
            category_title = "Good"
            category_index = "Current " + api['location']['name'] + " air quality index: " + str(
                api['current']['air_quality']['us_epa_index'])
            category_description = "Air quality is satisfactory, and air pollution poses little or no risk."
            category_color = "good"

        elif api['current']['air_quality']['us_epa_index'] == 2:
            category_title = "Moderate"
            category_index = "Current " + api['location']['name'] + " air quality index: " + str(
                api['current']['air_quality']['us_epa_index'])
            category_description = "Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
            category_color = "moderate"

        elif api['current']['air_quality']['us_epa_index'] == 3:
            category_title = "Unhealthy for sensitive group"
            category_index = "Current " + api['location']['name'] + " air quality index: " + str(
                api['current']['air_quality']['us_epa_index'])
            category_description = "Members of sensitive groups may experience health effects. The general public is less likely to be affected."
            category_color = "usg"

        elif api['current']['air_quality']['us_epa_index'] == 4:
            category_title = "Unhealthy"
            category_index = "Current " + api['location']['name'] + " air quality index: " + str(
                api['current']['air_quality']['us_epa_index'])
            category_description = "Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"

        elif api['current']['air_quality']['us_epa_index'] == 5:
            category_title = "Very Unhealthy"
            category_index = "Current " + api['location']['name'] + " air quality index: " + str(
                api['current']['air_quality']['us_epa_index'])
            category_description = "Health alert: The risk of health effects is increased for everyone."
            category_color = "veryunhealthy"

        elif api['current']['air_quality']['us_epa_index'] == 6:
            category_title = "Hazardous"
            category_index = "Current " + api['location']['name'] + " air quality index: " + str(
                api['current']['air_quality']['us_epa_index'])
            category_description = "Health warning of emergency conditions: everyone is more likely to be affected."
            category_color = "harzardous"

        return render(request, 'Home.html', {
            'api': api,
            'category_title': category_title,
            'category_index': category_index,
            'category_description': category_description,
            'category_color': category_color
        })

    else:

        api_request = requests.get("http://api.weatherapi.com/v1/current.json?key=078d7a99f6a54328abb71558221505&q"
                                   "=montreal&aqi=yes")
        try:
            api = json.loads(api_request.content)
            api['current']['air_quality']['us_epa_index'] = api['current']['air_quality']['us-epa-index']
            del api['current']['air_quality']['us-epa-index']

            api['current']['air_quality']['gb_defra_index'] = api['current']['air_quality']['gb-defra-index']
            del api['current']['air_quality']['gb-defra-index']

        except Exception as e:
            api = "Error..."

        if api['current']['air_quality']['us_epa_index'] == 1:
            category_title = "Good"
            category_index = "Current " + api['location']['name'] + " air quality index: " + str(api['current']['air_quality']['us_epa_index'])
            category_description = "Air quality is satisfactory, and air pollution poses little or no risk."
            category_color = "good"

        elif api['current']['air_quality']['us_epa_index'] == 2:
            category_title = "Moderate"
            category_index = "Current " + api['location']['name'] + " air quality index: " + str(api['current']['air_quality']['us_epa_index'])
            category_description = "Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
            category_color = "moderate"

        elif api['current']['air_quality']['us_epa_index'] == 3:
            category_title = "Unhealthy for sensitive group"
            category_index = "Current " + api['location']['name'] + " air quality index: " + str(api['current']['air_quality']['us_epa_index'])
            category_description ="Members of sensitive groups may experience health effects. The general public is less likely to be affected."
            category_color = "usg"

        elif api['current']['air_quality']['us_epa_index'] == 4:
            category_title = "Unhealthy"
            category_index = "Current " + api['location']['name'] + " air quality index: " + str(api['current']['air_quality']['us_epa_index'])
            category_description ="Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"

        elif api['current']['air_quality']['us_epa_index'] == 5:
            category_title = "Very Unhealthy"
            category_index = "Current " + api['location']['name'] + " air quality index: " + str(api['current']['air_quality']['us_epa_index'])
            category_description = "Health alert: The risk of health effects is increased for everyone."
            category_color = "veryunhealthy"

        elif api['current']['air_quality']['us_epa_index'] == 6:
            category_title = "Hazardous"
            category_index = "Current " + api['location']['name'] + " air quality index: " + str(api['current']['air_quality']['us_epa_index'])
            category_description = "Health warning of emergency conditions: everyone is more likely to be affected."
            category_color = "harzardous"

        return render(request, 'Home.html', {
            'api': api,
            'category_title': category_title,
            'category_index': category_index,
            'category_description': category_description,
            'category_color': category_color
            })


def about(request):
    return render(request, 'about.html', {})
