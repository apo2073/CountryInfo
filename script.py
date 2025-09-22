import requests

def get_ip_info():
    try:
        url = "http://ip-api.com/json/"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"ERROR: {e}")
        return None

def get_country_info(country_code):
    try:
        url = f"https://www.apicountries.com/alpha/{country_code}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"ERRROR: {e}")
        return None

def format_location_info():
    ip_data = get_ip_info()
    if not ip_data:
        return "Can't Read IP Info."

    ip = ip_data.get("query", "N/A")
    cc = ip_data.get("countryCode", "").lower()

    data = get_country_info(cc)
    if not data:
        return "Can't Read Country Info."

    lang = f"{data.get('languages', [{}])[0].get('iso639_1', 'N/A')}-{cc}"
    currencies = str(data.get("currencies", [{}])[0].get("code", "N/A"))

    return f"""
IP: {ip}
Region: {data.get("region", "N/A")}
Country ( Population ): {data.get("name", "N/A")}, {data.get("nativeName", "N/A")} ( {data.get("population", "N/A")} )
Country Code: {cc}
Language: {lang}
Timezone: {data.get("timezones", ["N/A"])[0]}
Currency: {currencies}
"""

def main():
    print(format_location_info())

if __name__ == "__main__":
    main()
