import unittest
import webbrowser
import Rekog

class UnitTest(unittest.TestCase):

    def test_rekog(self):

        vehicle = input('Please enter Vehicle Type: ')
        link = 'https://www.google.com/search?q=' + vehicle + '&rlz=1C1CHBF_enNZ763NZ763&sxsrf=ALeKk01bg-n7DJDmgZ-iATp3d27P1DzNdQ:1584143394995&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiX1dOC0pjoAhVqxDgGHTGMAFMQ_AUoAXoECA8QAw'
        webbrowser.open(link)
        pic = input('Please enter picture link: ')
        result = Rekog.rekog(pic, vehicle.lower())
        scd = ''
        if vehicle.lower() in result:
            scd = result
            self.assertEqual(result, scd)
        else:
            self.assertEqual(result, vehicle.lower())


if __name__ == '__main__':
    unittest.main()
