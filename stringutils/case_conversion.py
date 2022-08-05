from stringutils import split_at_uppercase


def to_snake_case(uppercase_title: str) -> str:
    """
    >>> to_snake_case('GenerativeModel')
    'generative_model'

    >>> to_snake_case('BernoulliVariationalAutoEncoder')
    'bernoulli_variational_auto_encoder' """

    return '_'.join(map(lambda string: string.lower(), split_at_uppercase(uppercase_title)))


def to_class_case(snake_case: str) -> str:
    """
    >>> to_class_case('linear_and_circular')
    'LinearAndCircular'

    >>> to_class_case('linear')
    'Linear' """

    return snake_case.replace('_', ' ').title().replace(' ', '')