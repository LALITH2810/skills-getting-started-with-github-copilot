import pytest
from httpx import AsyncClient
from src.app import app
from fastapi.testclient import TestClient

import asyncio

@pytest.mark.asyncio
async def test_get_activities():
    # Arrange
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Act
        response = await ac.get("/activities")
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data

@pytest.mark.asyncio
async def test_signup_and_unregister():
    # Arrange
    test_email = "testuser@mergington.edu"
    activity = "Art Club"
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Act: Sign up
        signup_resp = await ac.post(f"/activities/{activity}/signup?email={test_email}")
        # Assert: Signup
        assert signup_resp.status_code == 200
        assert f"Signed up {test_email}" in signup_resp.json()["message"]

        # Act: Unregister
        unregister_resp = await ac.post(f"/activities/{activity}/unregister?email={test_email}")
        # Assert: Unregister
        assert unregister_resp.status_code == 200
        assert f"Unregistered {test_email}" in unregister_resp.json()["message"]
