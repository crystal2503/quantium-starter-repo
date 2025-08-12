import pytest
from dash.testing.application_runners import import_app

@pytest.fixture
def dash_app():
    app = import_app('app')  # assumes your app is in app.py
    return app

def test_header_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    header = dash_duo.find_element('h1')
    assert header.text == 'Soul Foods Pink Morsel Sales Visualiser'

def test_visualisation_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    graph = dash_duo.find_element('#sales-line-chart')
    assert graph is not None

def test_region_picker_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    radio_items = dash_duo.find_element('#region-radio')
    assert radio_items is not None
