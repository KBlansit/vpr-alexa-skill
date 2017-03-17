from unittest.mock import patch

from tests.fixtures import mock_vt_ed
from vpr_alexa import programs


@patch('vpr_alexa.programs._get_feed', return_value=mock_vt_ed)
def test_latest_vt_edition(mock):
    """
    Make sure we can fetch the latest episode from the podcast feed and get
    its metadata
    """
    program = programs.latest_episode('vermont edition')
    assert program.name == 'Vermont Edition'
    assert program.title == 'This is a pretend Vermont Edition'
    assert program.url == 'https://cpa.ds.npr.org/vpr/audio/2017/03/vted.mp3'
