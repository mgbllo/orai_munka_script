import unittest
import app
import db
import sample


class DBTests(unittest.TestCase):

    def setUp(self):
        self.app = app.createTestClient()
        self.db = db.create_db_connection()

    def test_site_health_check(self):
        response = self.app.get('/ping')
        self.assertEqual(response.data, b'1')

    def test_x_database_exists(self):
        self.assertIn(db.DB_NAME, self.db.list_database_names())

    def test_add_route_data_correct_jarat1(self):
        db.init_database()
        response = self.app.post(
            '/add-route-data/jarat1', json=sample.get_sample_data(),
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'data saved')

    def test_add_route_data_jarat2(self):
        response = self.app.post(
            '/add-route-data/jarat2', json=sample.get_sample_data(),
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'data saved')

    def test_add_route_data_jarat3(self):
        response = self.app.post(
            '/add-route-data/jarat3', json=sample.get_sample_data(),
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'data saved')

    def test_upload_incorrect(self):
        response = self.app.post(
            '/add-route-data', json=sample.get_sample_data(),
            content_type='application/json')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
