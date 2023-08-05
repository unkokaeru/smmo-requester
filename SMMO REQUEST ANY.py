"""hello."""

# Disclaimer: This python script was created using the aid of ChatGPT.
# All credit should be attributed to ChatGPT and its creators.

import json

import requests

# API KEY
API_KEY = (
    "DUAjalpWHAbk9sxI7f9rOGXw5GI96LK44UsTvvm2Xt5R3JQqEI6Ue33YPpLpkKr43qd7WrbUI9QNfFsP"
)

# IDs, if not known, run and select option 2
PLAYER_ID = 1019244
GUILD_ID = 2746
ITEM_ID = 1

# API Options
options = {
    "Player Information": f"https://api.simple-mmo.com/v1/player/info/{PLAYER_ID}",
    "Your Information": "https://api.simple-mmo.com/v1/player/me",
    "Player Equipped Items": f"https://api.simple-mmo.com/v1/player/equipment/{PLAYER_ID}",
    "Player Skills": f"https://api.simple-mmo.com/v1/player/skills/{PLAYER_ID}",
    "Diamond Market": "https://api.simple-mmo.com/v1/diamond-market",
    "Orphanage": "https://api.simple-mmo.com/v1/orphanage",
    "World Bosses": "https://api.simple-mmo.com/v1/worldboss/all",
    "Item Information": f"https://api.simple-mmo.com/v1/item/info/{ITEM_ID}",
    "List of Guilds": "https://api.simple-mmo.com/v1/guilds/all",
    "Guild Information": f"https://api.simple-mmo.com/v1/guilds/info/{GUILD_ID}",
    "Guild Members": f"https://api.simple-mmo.com/v1/guilds/members/{GUILD_ID}",
    "Guild Member Contribution": f"https://api.simple-mmo.com/v1/guilds/members/{GUILD_ID}/contribution/{PLAYER_ID}",
    "Guild Wars": f"https://api.simple-mmo.com/v1/guilds/wars/{GUILD_ID}/4",
    "Guild Seasons": "https://api.simple-mmo.com/v1/guilds/seasons",
    "Guild Season 1 Leaderboards": "https://api.simple-mmo.com/v1/guilds/seasons/1",
    "Guild Season 2 Leaderboards": "https://api.simple-mmo.com/v1/guilds/seasons/2",
}


def fetch_data(choice: int) -> str:
    """
    Fetches any data requested from the SimpleMMO API.

    Parameters:
    choice (int): The number choice chosen from the menu.
    """
    request = requests.post(
        f"{list(options.items())[choice - 1][1]}", data={"api_key": API_KEY}, timeout=1
    )
    if request.status_code == 200:
        formatted_request = json.dumps(json.loads(request.text), indent=2)
    else:
        formatted_request = "Error: cannot fetch data from API."

    x_rate_limit_limit = request.headers.get("X-RateLimit-Limit")
    x_rate_limit_remaining = request.headers.get("X-RateLimit-Remaining")
    print(
        (
            f"You have {x_rate_limit_remaining}"
            f"/{x_rate_limit_limit} requests remaining within this minute.\n"
        )
    )

    return formatted_request


def main() -> None:
    """
    The main() function offers a menu of options to the user to choose from.
    It then passes the user's choice to the fetch_data() and collect_data() functions.
    It also includes validation for the user input and recursively calls itself
    if an invalid option is selected.
    """

    # Print menu options
    for item, url in options.items():
        print(f"{list(options.keys()).index(item) + 1}. {item.title()}")

    # Take user option choice
    user_choice = int(input(f"Enter your choice [1-{len(options)}] : "))

    # Validate user input
    if user_choice < 1 or user_choice > len(options):
        print("Invalid choice, try again.\n")
        # Recursively invoke main()
        main()
    else:
        # Call the appropriate function
        print(" ")
        data = fetch_data(user_choice)

    print(data)


if __name__ == "__main__":
    main()
