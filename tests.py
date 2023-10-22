import unittest
import requests

class TestAPI(unittest.TestCase):
    def setUp(self):
        # Define the base URL of endpoint
        self.base_url = 'http://127.0.0.1:8080/'

        # Define test cases with usernames and expected item counts
        self.test_cases = [
            {'username': 'octocat', 'expected_count': 8},
            {'username': 'Bono-gist-test-lt-1mb', 'expected_count': 1}
        ]

    def test_get_user_data(self):
        for test_case in self.test_cases:
            username = test_case['username']
            expected_count = test_case['expected_count']
            print(f"About to test User: {username}, expected count {expected_count}", flush=True)

            # Make a GET request to the API endpoint
            response = requests.get(self.base_url + username)

            # Check the response status code
            self.assertEqual(response.status_code, 200)

            # Check if the response content is in JSON format
            self.assertTrue(response.headers['content-type'].lower().startswith('application/json'))

            # Parse the JSON response
            user_data = response.json()

            # Check the expected item count
            item_count=len(user_data['gists'])
            self.assertEqual(item_count, expected_count)
            print(f"User: {username}, expected count {expected_count}, received count {item_count}",flush=True)


if __name__ == '__main__':
    unittest.main()
