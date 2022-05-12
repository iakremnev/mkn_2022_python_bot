# these are effects of text, which available by means of text characters
# effects not stacks, only external effect will be applying

def italics(text: str) -> str:
    """Makes text italics"""
    return "__" + text + "__"


def bold(text: str) -> str:
    """Makes text bold"""
    return "**" + text + "**"


def hidden(text: str) -> str:
    """Makes text hidden"""
    return "||" + text + "||"


def monospaced(text: str) -> str:
    """Makes text monospaced"""
    return "`" + text + "`"


def crossed(text: str) -> str:
    """Makes test crossed out"""
    return "~~" + text + "~~"
