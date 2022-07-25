from pathlib import Path
import random


def _catsay(
    text: str,
    reverse: bool = False,
    filepath: Path = Path(__file__).parent / "img/",
) -> str:
    """the cat says...
    args and kwargs to pass to print"""
    imgs = [i for i in filepath.glob("cat*")]
    # select random cat image
    cat = imgs[random.choice(range(len(imgs)))]
    # read cat image
    with cat.open() as f:
        img = f.read()

    img = reverse_img(img) if reverse else img
    return chat_bubble(text) + "\n" + img


def catsay(
    text: str,
    reverse: bool = False,
    filepath: Path = Path(__file__).parent / "img/",
    *args,
    **kwargs
) -> None:
    print(_catsay(text, reverse, filepath), *args, **kwargs)


def chat_bubble(text: str) -> str:
    """make the chat bubble"""
    width = max([len(l) for l in text.split("\n")])
    bubble = [
        " / " + "-" * width + " \ ",
        *["| " + l + " " * (width - len(l) + 2) + " |" for l in text.split("\n")],
        " \ " + "-" * width + " / ",
        " " * 3 + "V",
    ]
    return "\n".join(bubble)


def reverse_img(img: str, buffer: int = 10) -> str:
    """reverse the cat image"""
    # find max line len
    max_ = 0
    # strip all whitespace from the right of the image
    lines = [l.rstrip(" ") for l in img.split("\n")]
    for l in lines:
        if len(l) > max_:
            max_ = len(l)
    # print(max_)

    # ensure all images are padded to same line length
    pad_img = []
    for l in lines:
        pad_img.append(l + " " * (max_ - len(l)))

    # lookup to reverse chars
    pairs = ["{}", "[]", "()", "\/", "><"]
    lookup = {**{k: v for k, v in pairs}, **{v: k for k, v in pairs}}

    # reverse the img
    rev = []
    for l in pad_img:
        rev.append(
            " " * buffer
            + "".join([lookup[c] if c in lookup else c for c in reversed(l)])
        )

    return "\n".join(rev)


if __name__ == "__main__":

    text = "there once was a man\nfrom nantucket\nwho had a kitten named nugget"
    catsay(text)
