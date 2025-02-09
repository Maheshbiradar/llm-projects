import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    print(linkedin_profile_url)
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/Maheshbiradar/c66fb0d7df491263e1cdc3ff85ef1b96/raw/0120d0b772b6412b3c3b838566285243604c3757/gistfile1.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/company"
        params = {
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": linkedin_profile_url,
        }
        response = requests.get(
            api_endpoint,
            params=params,
            timeout=10,
        )

    data = response.json().get("company")

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None) and k not in ["certifications"]
    }
    return data

if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/company/ntt-data-inc/"
        ),
    )