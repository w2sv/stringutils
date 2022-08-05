import hashlib
import re
from typing import List


def split_at_uppercase(string: str) -> List[str]:
    """
    >>> split_at_uppercase('GenerativeModel')
    ['Generative', 'Model'] """

    return re.findall('[A-Z][^A-Z]*', string)


def unique_hash(s: str, digits=16) -> int:
    """ Returns:
            string hash being consistent across runs """

    return int(
        hashlib.sha256(s.encode('utf-8')).hexdigest(),
        16
    ) % 10 ** digits