from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import events_filter
import json
import sys
import exceptions


def call_github_api(username: str) -> tuple[dict, int]:
    """
    Calls the GitHub API with the username provided to obtain the latest user
    activity and send it as a list to filter_github_activity to filter it
    by repo and event type
    :param: A valid GitHub username
    :return: A tuple containing a dictionary and an integer
    """
    try:
        with urlopen(
                f'https://api.github.com/users/{username}/events',
                timeout=10
        ) as response:
            return events_filter.filter_github_activity(json.load(response))

    except HTTPError as e:
        if e.code == 404:
            raise exceptions.UserNotFound(f"User {username} not found") from e
        elif e.code == 403:
            raise exceptions.ApiLimitRate("API rate limit exceeded") from e
        else:
            raise exceptions.GitHubApiError(f"Unexpected API error > {e.code}") from e

    except URLError as e:
        raise ConnectionError("Connection error") from e

def main(username: str):
    """
    Calls the call_github_api with the username obtained from the CLI and print
    the repo names with their respective events and a total of activities
    :param: A valid GitHub username
    """
    try:
        user_events, total_events = call_github_api(username)

        print(f"*****************************\n"
              f"{username} Recent Activity\n"
              f"Total events: {total_events}\n"
              f"*****************************")

        for repo, v in user_events.items():
            print(f"Repository [{repo}]:")
            for event, x in v.items():
                print(f"{event}: {x}")
            print("*****************************")

    except exceptions.UserNotFound as e:
        print(f"Error: {e}")
    except exceptions.ApiLimitRate as e:
        print(f"Error: {e}")
    except exceptions.GitHubApiError as e:
        print(f"Error: {e}")
    except ConnectionError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    if len(sys.argv) > 0:
        main(sys.argv[1])
    else:
        print("Provide a GitHub username")