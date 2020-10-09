import random

from human_readable_ids.nouns import get_nouns
from human_readable_ids.adjectives import get_adjectives


def get_new_id(with_number=True):
    id_ = f"{random.choice(get_adjectives()).capitalize()} {random.choice(get_nouns()).capitalize()}"
    if with_number:
        id_ += f" {random.randrange(1, 100)}"
    return id_
