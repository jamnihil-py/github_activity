class GitHubApiError(Exception):
    """
    A class to handle GitHub related errors
    """
    pass

class UserNotFound(GitHubApiError):
    """
    A class that handles the 404 User Not Found error
    """
    pass

class ApiLimitRate(GitHubApiError):
    """
    A class that handles the GitHub API Limit error
    """
    pass