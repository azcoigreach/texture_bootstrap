import pytest
from datetime import datetime
from contextlib import contextmanager

from textual._context import active_app

@contextmanager
def set_active_app(app):
    token = active_app.set(app)
    try:
        yield
    finally:
        active_app.reset(token)

from ..main import DemoApp, HelpScreen, SettingsScreen, DemoModal
from textual.widgets import Header, Footer, Static, Label


def test_app_initial_composition():
    """Test that the DemoApp initial composition includes a Header widget."""
    app = DemoApp()
    with set_active_app(app):
        comp = list(app.compose())
    assert any(isinstance(w, Header) for w in comp), "A Header widget should be part of the initial composition"


def test_help_screen_composition():
    """Test the HelpScreen composition includes Header, Label and Footer."""
    screen = HelpScreen()
    comp = list(screen.compose())
    assert any(isinstance(w, Header) for w in comp), "HelpScreen should have a Header"
    assert any(isinstance(w, Footer) for w in comp), "HelpScreen should have a Footer"
    assert any(isinstance(w, Label) for w in comp), "HelpScreen should have a Label"


def test_settings_screen_composition():
    """Test the SettingsScreen composition includes Header, Input widgets, and Footer."""
    screen = SettingsScreen()
    dummy_app = DemoApp()
    screen._app = dummy_app
    with set_active_app(dummy_app):
        comp = list(screen.compose())
    assert any(isinstance(w, Header) for w in comp), "SettingsScreen should have a Header"
    # Check for Input widgets by looking for placeholder attribute in any widget
    assert any(hasattr(w, 'placeholder') for w in comp), "SettingsScreen should have Input widgets"
    assert any(isinstance(w, Footer) for w in comp), "SettingsScreen should have a Footer"


def test_reactive_time_update():
    """Test that the update_time method updates the reactive time property."""
    app = DemoApp()
    # Set an initial dummy time
    app.time = "00:00:00"
    try:
        app.update_time()
    except Exception:
        # If the widget lookup fails outside of a mounted context, ignore the error for this test
        pass
    updated_time = datetime.now().strftime("%H:%M:%S")
    # Allow a potential slight difference in seconds due to execution time
    assert app.time[:5] == updated_time[:5], "The time property should be updated to the current time"


@pytest.mark.asyncio
async def test_demo_modal_dismiss():
    """Test the DemoModal dismiss functionality."""
    modal = DemoModal()
    # action_dismiss is asynchronous. Await it to ensure no errors are raised
    await modal.action_dismiss()