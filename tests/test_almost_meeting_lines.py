#!/usr/bin/python3

import unittest

from src.almost_meeting_lines import almost_meeting_lines


class AlmostMeetingLines(unittest.TestCase):

    def test_types(self):
        a1 = 1
        b1 = 4
        a2 = 3
        b2 = 2
        p = (a1, b1, a2, b2)
        system = "(a1=%i, b1=%i, a2=%i, b2=%i)" % p
        (x, y), exact = almost_meeting_lines(*p)
        self.assertIsInstance(
            exact, bool,
            msg=f"Expected the exact value to be a bool. Got {type(exact)}.")
        self.assertIsInstance(
            y, float,
            msg=f"Expected the y coordinate to have type float! Got {type(y)}.")
        self.assertIsInstance(
            x, float,
            msg=f"Expected the x coordinate to have type float! Got {type(x)}.")

    def test_first(self):
        a1 = 1
        b1 = 4
        a2 = 3
        b2 = 2
        p = (a1, b1, a2, b2)
        system = "(a1=%i, b1=%i, a2=%i, b2=%i)" % p
        (x, y), exact = almost_meeting_lines(*p)
        self.assertEqual(exact, True, msg="Expected exact solution for system %s!" % system)
        self.assertAlmostEqual(
            y, a1 * x + b1,
            msg="Solution %f does not satisfy the first equation of system %s!" % (y, system))
        self.assertAlmostEqual(
            y, a2 * x + b2,
            msg="Solution %f does not satisfy the second equation of system %s!" % (y, system))

    def test_underdetermined(self):
        a1 = 1
        b1 = 4
        p = (a1, b1, a1, b1)
        system = "(a1=%i, b1=%i, a2=%i, b2=%i)" % p
        (x, y), exact = almost_meeting_lines(*p)
        self.assertEqual(
            exact, False,
            msg="Did not expect exact solution for underdetermined system %s!" % system)

    def test_inconsistent(self):
        a1 = 1
        b1 = 4
        p = (a1, b1, a1, b1 + 1)
        system = "(a1=%i, b1=%i, a2=%i, b2=%i)" % p
        (x, y), exact = almost_meeting_lines(*p)
        self.assertEqual(
            exact, False,
            msg="Did not expect exact solution for inconsistent system %s!" % system)


if __name__ == '__main__':
    unittest.main()
