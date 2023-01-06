import unittest
import Otplast


# from otp import generate_otp


class TestgenerateOTP(unittest.TestCase):

    def testcase1(self):
        size = 4

        #To Check Otp
        res = Otplast.otp(4)
        self.assertEqual(len(res), size)

        #To Check email address for sender
        Email = Otplast.emailsender
        self.assertIn("@",Email)
        self.assertIn(".",Email)
        self.assertIn("com",Email)

        #To Check email address for reciver
        Email2 = Otplast.emailreciver
        self.assertIn("@",Email2)
        self.assertIn(".",Email2)
        self.assertIn("com",Email2)



    def testcase2(self):
        size = 4

        # To Check Otp
        res = Otplast.otp(4)
        self.assertEqual(len(res), size)

        # To Check email address
        Email = Otplast.emailsender
        self.assertIn("@", Email)
        self.assertIn(".", Email)
        self.assertIn("com", Email)

    def testcase3(self):
        size = 4

        # To Check Otp
        res = Otplast.otp(4)
        self.assertEqual(len(res), size)

        # To Check email address
        Email = Otplast.emailsender
        self.assertIn("@", Email)
        self.assertIn(".", Email)
        self.assertIn("com", Email)

        #To Check email address for reciver
        Email2 = Otplast.emailreciver
        self.assertIn("@",Email2)
        self.assertIn(".",Email2)
        self.assertIn("com",Email2)

    def testcase4(self):
        size = 4

        # To Check Otp
        res = Otplast.otp(4)
        self.assertEqual(len(res), size)

        # To Check email address
        Email = Otplast.emailsender
        self.assertIn("@", Email)
        self.assertIn(".", Email)
        self.assertIn("com", Email)

        #To Check email address for reciver
        Email2 = Otplast.emailreciver
        self.assertIn("@",Email2)
        self.assertIn(".",Email2)
        self.assertIn("com",Email2)




if __name__ == '__main__':

    unittest.main()
