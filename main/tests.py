from django.test import TestCase

# Create your tests here.
class CtrlFARTestCase(TestCase):
    def tests_work(self):
        """Test to see if tests work in project"""
        red = 'red'
        blue = 'blue'
        yellow = 'yellow'
        black = False
        if (red and blue and yellow):
            black = True
        self.assertEqual(black, True)
