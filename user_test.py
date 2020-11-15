import unittest
from user import User
from credentials import Account

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Vivine", "Mutoni", "MVivi", "viviMuto")


    def test_init(self):
        self.assertEqual(self.new_user.first_name, "Vivine")
        self.assertEqual(self.new_user.last_name, "Mutoni")
        self.assertEqual(self.new_user.user_name, "Mvivi")
        self.assertEqual(self.new_user.password, "viviMuto")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user listed
        '''
        self.new_user.save_user() 
        self.assertEqual(len(User.user_list),1)


    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''

            User.user_list = []


    def test_save_multiple_users(self):

        '''
        test_save_multiple_users to check if we can save multiple user
        objects to our user_list
        '''
        
        self.new_user.save_user()
        test_user = User("Henry", "Ian", "Hian", "lifesgood")
        test_user.save_user()

        self.assertEqual(len(User.user_list),2)


    def test_delete_user(self):
        '''
        test_delete_user to test if we van remove a user from our user list
        '''

        self.new_user.save_user()
        test_user = User("Robert", "Nesta", "NErob", "jahbless")
        test_user.save_user()

        self.new_user.delete_user() 
        self.assertEqual(len(User.user_list),1)


    def test_find_user_by_username(self):
        '''
        test to check if we can find a user by their username and display infformation
        '''

        self.new_user.save_user()
        test_user = User("Maya", "Angelou", "MAyang", "untoldstory")
        test_user.save_user()

        found_user = User.find_by_username("MAyang")
        self.assertEqual(found_user.user_name,"MAyang")


    def test_find_user_by_password(self):
        '''
        test to check if we can find a user by their password
        '''

        self.new_user.save_user()
        test_user = User("Cicely", "Tyson", "CTyson", "thesound")
        test_user.save_user()

        found_password = User.find_by_userpassword("thesound")
        self.assertEqual(found_password.password,"thesound")


    def test_display_user_information(self):
        '''
        test to check if we can be able to display users saved in user_list
        '''

        self.assertEqual(User.display_userInfo(),User.user_list)

        
if __name__ == '__main__':
    unittest.main()




