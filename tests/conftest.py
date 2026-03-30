from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


INITIAL_ACTIVITIES = deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    # Arrange: restore the in-memory data before each test.
    activities.clear()
    activities.update(deepcopy(INITIAL_ACTIVITIES))

    yield

    # Assert isolation by resetting again after each test.
    activities.clear()
    activities.update(deepcopy(INITIAL_ACTIVITIES))


@pytest.fixture()
def client():
    with TestClient(app) as test_client:
        yield test_client