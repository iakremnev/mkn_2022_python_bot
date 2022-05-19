# if you set escape flag True, re-escaped text will be incorrect
def escape(text: str, escape_slash: bool = False) -> str:
    """
    Escape with '\\' all symbols with code 1 to 126 and special symbols:
    '_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!'.

    :param text: his special characters will be escaped
    :param escape_slash: if you set this flag True a character '\' also will be escaped. For example, double
     applying escape to text='*' returns '\\\*'. It will imagine in message like '\*'.
    """
    escaped_symbols = "_*[]()~`>#+-=|{}.!\\"

    replace = {k: "\\" + k for k in escaped_symbols}
    if not escape_slash:
        replace["\\"] = ""

    result = ""
    for c in text:
        if c in replace:
            result += replace[c]
        else:
            result += c
    return result

# these effects may stack, set escape_interior False to not escape text before applying effect
# use it with markdown_v2


def italics(text: str, escape_interior: bool = True) -> str:
    """Makes text italics"""
    if escape_interior:
        text = escape(text)
    return "_" + text + "_"


def bold(text: str, escape_interior: bool = True) -> str:
    """Makes text bold"""
    if escape_interior:
        text = escape(text)
    return "*" + text + "*"


def hidden(text: str, escape_interior: bool = True) -> str:
    """Makes text hidden"""
    if escape_interior:
        text = escape(text)
    return "||" + text + "||"


def monospaced(text: str, escape_interior: bool = True) -> str:
    """Makes text monospaced"""
    if escape_interior:
        text = escape(text)
    return "`" + text + "`"


def crossed(text: str, escape_interior: bool = True) -> str:
    """Makes test crossed out"""
    if escape_interior:
        text = escape(text)
    return "~" + text + "~"


def underlined(text: str, escape_interior: bool = True) -> str:
    """Makes text underlined"""
    if escape_interior:
        text = escape(text)
    return "__" + text + "\r__"

# this function apply stack of effects to text


def multi_effects(
        text: str, *,
        b: bool = False,
        it: bool = False,
        h: bool = False,
        ms: bool = False,
        cr: bool = False,
        ul: bool = False,
        escaped: bool = True
) -> str:
    """
    Apply many effects to text. By default, escaped text before.

    :param text: apply all effects to it
    :param b: bold effect
    :param it: italics effect
    :param h: hidden effect
    :param ms: monospaced effect
    :param cr: crossed effect
    :param ul: underlined effect
    :param escaped: escape interior text
    """
    result = text
    if escaped:
        result = escape(result)
    if b:
        result = bold(result, False)
    if it:
        result = italics(result, False)
    if h:
        result = hidden(result, False)
    if ms:
        result = monospaced(result, False)
    if cr:
        result = crossed(result, False)
    if ul:
        result = underlined(result, False)
    return result
