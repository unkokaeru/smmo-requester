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
player_id = 1019244
guild_id = 2746
item_id = 1

# API Options
options = {
    "Player Information": f"https://api.simple-mmo.com/v1/player/info/{player_id}",
    "Your Information": "https://api.simple-mmo.com/v1/player/me",
    "Player Equipped Items": f"https://api.simple-mmo.com/v1/player/equipment/{player_id}",
    "Player Skills": f"https://api.simple-mmo.com/v1/player/skills/{player_id}",
    "Diamond Market": "https://api.simple-mmo.com/v1/diamond-market",
    "Orphanage": "https://api.simple-mmo.com/v1/orphanage",
    "World Bosses": "https://api.simple-mmo.com/v1/worldboss/all",
    "Item Information": f"https://api.simple-mmo.com/v1/item/info/{item_id}",
    "List of Guilds": "https://api.simple-mmo.com/v1/guilds/all",
    "Guild Information": f"https://api.simple-mmo.com/v1/guilds/info/{guild_id}",
    "Guild Members": f"https://api.simple-mmo.com/v1/guilds/members/{guild_id}",
    "Guild Member Contribution": f"https://api.simple-mmo.com/v1/guilds/members/{guild_id}/contribution/{player_id}",
    "Guild Wars": f"https://api.simple-mmo.com/v1/guilds/wars/{guild_id}/4",
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
        f"{list(options.items())[choice - 1][1]}",
        data={"api_key": API_KEY},
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
