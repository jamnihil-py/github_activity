import urllib.request
import events_filter
import json
import sys

def call_github_api(username: str) -> tuple[dict, int]:
    """
    Calls the GitHub API with the username provided and sends the data to
    function [function] to process and filter the type events
    :param: Username
    :return: A tuple containing two dictionaries ???
    """
    with urllib.request.urlopen(
            f'https://api.github.com/users/{username}/events',
            timeout=10
    ) as response:
        github_data = json.load(response)

    return events_filter.filter_github_activity(github_data)

def main(username: str):
    """

    :return:
    """
    user_events, total_events = call_github_api(username)

    print(f"*****************************\n"
          f"{username} Recent Activity:\n"
          f"Total events: {total_events}\n"
          f"*****************************")

    for repo, v in user_events.items():
        print(f"Repository [{repo}]:")
        for event, x in v.items():
            print(f"{event}: {x}")
        print("*****************************")


if __name__ == '__main__':
    if len(sys.argv) > 0:
        main(sys.argv[1])
    else:
        print("Provide a GitHub username")