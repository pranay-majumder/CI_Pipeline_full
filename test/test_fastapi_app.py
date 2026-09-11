import unittest

from fastapi.testclient import TestClient

from fastapi_app.app import app


# Create Test Client

# TestClient can call your FastAPI endpoints without starting the FastAPI server with Uvicorn.

# Test code
#    ↓
# TestClient
#    ↓
# FastAPI `app` object
#    ↓
# POST /predict
#    ↓
# predict() function
#    ↓
# Response

# There is no Uvicorn and no localhost:8000 involved.

client = TestClient(app)


class TestFastAPI(unittest.TestCase):

    # Test positive sentiment
    def test_predict_happy(self):
        response = client.post(
            "/predict",
            json={"text": "I love this product!"}
        )

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(data["text"], "I love this product!")
        self.assertIn("processed_text", data)
        self.assertEqual(data["sentiment"], "happy")


    # Test negative sentiment
    def test_predict_sad(self):
        response = client.post(
            "/predict",
            json={"text": "I hate this product!"}
        )

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(data["text"], "I hate this product!")
        self.assertIn("processed_text", data)
        self.assertEqual(data["sentiment"], "sad")


    # Test response structure
    def test_response_structure(self):
        response = client.post(
            "/predict",
            json={"text": "This is good"}
        )

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertIn("text", data)
        self.assertIn("processed_text", data)
        self.assertIn("sentiment", data)


    # Test missing text field
    def test_missing_text(self):
        response = client.post(
            "/predict",
            json={}
        )

        self.assertEqual(response.status_code, 422)


    # Test invalid text type
    def test_invalid_text_type(self):
        response = client.post(
            "/predict",
            json={"text": 12345}
        )

        self.assertEqual(response.status_code, 422)


    # Test empty text
    def test_empty_text(self):
        response = client.post(
            "/predict",
            json={"text": ""}
        )

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()