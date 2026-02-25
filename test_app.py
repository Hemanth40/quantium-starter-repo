import pytest
import chromedriver_autoinstaller
from dash.testing.application_runners import import_app

chromedriver_autoinstaller.install()

app = import_app("app")

def test_header_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("#title")
    assert header is not None

def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-graph")
    assert graph is not None

def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    radio = dash_duo.find_element("#region-filter")
    assert radio is not None
