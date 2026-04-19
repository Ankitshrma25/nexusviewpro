"""
custom exception file
"""

class NexusViewProError(Exception):
    """
    Base class for all NexusViewPro exception
    """

    pass

# URL Validation errors
class InvalidURLError(NexusViewProError):
    """
    This is raised when a URL is Empty, malformed, or used an unsopported scheme.
    """
    def __init__(self, url: str, reason: str = "") -> None:
        self.url = url
        self.reason = reason

        message = f"Invalid URL: '{url}'"
        if reason:
            message += f" - {reason}"

        super().__init__(message)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"url={self.url!r}, reason={self.reason!r})"
        )
    

# YouTube specefic errors

class VideoIDExtractionError(NexusViewProError):
    """
    Raised when a YOUTUBE video id can't be paresed from the given url
    """

    def __init__(self, url: str) -> None:
        self.url = url
        super().__init__(
            f"could not extract YouTube video ID from: '{url}'. "
            "Supported formats: watch?v=, youtu.be/, /embed/, /shorts/"
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(url={self.url!r})"
    

# Rendering Errors

class RanderError(NexusViewProError):

    """
    Raised when an IPython display operation fails unexpectedly.    
    """

    def __init__(self, context: str, detail: str = "") -> None:
        self.context = context
        self.detail = detail

        message = f"Rendering failed in '{context}'"
        if detail:
            message += f": {detail}"
        
        super().__init__(message)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"context={self.context!r}, detail={self.detail!r})"
        )