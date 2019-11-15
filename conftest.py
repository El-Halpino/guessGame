import myApp
import pytest
import myApp as webapp


@pytest.fixture
def app():
    app = webapp.app
    return app
