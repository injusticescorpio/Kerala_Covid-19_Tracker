import requests
import json

response = requests.get('https://api.covid19india.org/state_district_wise.json').json()
kerala_details = response['Kerala']


class Covid_19():
    def __init__(self, district):
        self.district = district

    def covid_19_details_total(self):
        for i in kerala_details['districtData'].items():
            if i[0] == self.district.title():
                return (
                    f"{self.district} details so far\nActive cases:   {i[1]['active']}\nConfirmed Cases:{i[1]['confirmed']}\nDeaths by:{i[1]['deceased']}\nRecovered by:{i[1]['recovered']}")
        return ('No such districts in kerala!Check whether your spellings are correct')

    def covid_19_details_current(self):
        for i in kerala_details['districtData'].items():
            if i[0] == self.district.title():
                return (
                    f"{self.district} todays details so far\nConfirmed Cases:{i[1]['delta']['confirmed']}\nDeaths by:{i[1]['deceased']}\nRecovered by:{i[1]['delta']['recovered']}")
        return ('No such districts in kerala!Check whether your spellings are correct')

    def total_covid_19(self):
        total_confirmed = 0
        total_recovered = 0
        total_death = 0
        for i in kerala_details['districtData'].items():
            total_confirmed += i[1]['delta']['confirmed']
            total_recovered += i[1]['delta']['recovered']
            total_death += i[1]['delta']['deceased']
        if (total_confirmed == 0 and total_recovered == 0 and total_death == 0):
            return ("Sorry I didn't get the information yet! Please Try after sometime ")
        return (
            f"Today's Total confirmed:  {total_confirmed}\n Today's Total Recovered:  {total_recovered}\n Today's Total Deaths:  {total_death}")

