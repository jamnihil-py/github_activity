def filter_github_activity(events: list) -> tuple[dict, int]:
    """
    Filter the GitHub data sent by the function call_github_api to keep repos,
    event types and the total of activities
    :param events: List of EventTypes sent by the function call_github_api
    :return: user_repos_and_events = {repo_name: {event_type: 0}}
            total_events: How many events are in total
    """
    user_repos_and_events = {}
    total_events = 0

    for x in events:
        event_type = x['type']
        repo_name = x['repo']['name']
        user_repos_and_events.setdefault(repo_name, {}).setdefault(event_type, 0)
        user_repos_and_events[repo_name][event_type] += 1
        total_events += 1
    return user_repos_and_events, total_events