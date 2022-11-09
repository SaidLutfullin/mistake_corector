import unittest
from main import check_answer

class CheckAnswerTestCase(unittest.TestCase):
       
    def test_correct(self):
        result = check_answer('qwerty','qwerty', '<', '>')
        self.assertEqual(result, 1)

    def test_typo(self):
        result = check_answer('qw*rty','qwerty', '<', '>')
        self.assertEqual(result, 'qw<e>rty')

    def test_swap(self):
        result = check_answer('qwrety','qwerty', '<', '>')
        self.assertEqual(result, 'qw<er>ty')

    def test_skip(self):
        result = check_answer('qwrty','qwerty', '<', '>')
        self.assertEqual(result, 'qw<e>rty')

    def test_extra(self):
        result = check_answer('qwe*rty','qwerty', '<', '>')
        self.assertEqual(result, 'qw<er>ty')

    def test_begin_typo(self):
        result = check_answer('*werty','qwerty', '<', '>')
        self.assertEqual(result, '<q>werty')

    def test_begin_swap(self):
        result = check_answer('wqerty','qwerty', '<', '>')
        self.assertEqual(result, '<qw>erty')

    def test_begin_skip(self):
        result = check_answer('werty','qwerty', '<', '>')
        self.assertEqual(result, '<q>werty')

    def test_begin_extra(self):
        result = check_answer('*qwerty','qwerty', '<', '>')
        self.assertEqual(result, '<q>werty')

    def test_end_typo(self):
        result = check_answer('qwert*','qwerty', '<', '>')
        self.assertEqual(result, 'qwert<y>')

    def test_end_swap(self):
        result = check_answer('qweryt','qwerty', '<', '>')
        self.assertEqual(result, 'qwer<ty>')

    def test_end_skip(self):
        result = check_answer('qwert','qwerty', '<', '>')
        self.assertEqual(result, 'qwert<y>')

    def test_end_extra(self):
        result = check_answer('qwerty*','qwerty', '<', '>')
        self.assertEqual(result, 'qwert<y>')

    def test_two_symbol_missed_near(self):
        result = check_answer('q**rty','qwerty', '<', '>')
        self.assertEqual(result, 0)

    def test_two_symbol_missed(self):
        result = check_answer('q*er*y','qwerty', '<', '>')
        self.assertEqual(result, 0)

    def test_completely_wrong(self):
        result = check_answer('asdfgh','qwerty', '<', '>')
        self.assertEqual(result, 0)

    def test_inverted(self):
        result = check_answer('ytrewq','qwerty', '<', '>')
        self.assertEqual(result, 0)
