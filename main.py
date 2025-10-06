import urllib.request
import events_filter
import json

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

if __name__ == '__main__':
    main('srid')