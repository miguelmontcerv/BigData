import unittest

import mapper


class TestMapper(unittest.TestCase):
    # ["Word", "True", "David", "True"] => "word": 1, "True": 1
    # def test_returns_map_by_word
    def test_returns_a_map_with_every_word_as_key_and_one_as_value(self):
        input = "Word True David True"
        expected_out="Word\t1\nTrue\t1\nDavid\t1\nTrue\t1\n"
        self.assertEqual(mapper.mapper(input), expected_out)

