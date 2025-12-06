from homework.src._internals.preprocess_lines import preprocess_lines


def test_preprocess_lines():
    lines = [" Hello, World!  ", "Python is GREAT."]
    preprocessed = preprocess_lines(lines)
    assert preprocessed == ["hello, world!", "python is great."]
