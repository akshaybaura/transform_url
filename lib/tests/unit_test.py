import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from transformer import Transformer

def test_get_hostname_from_url():
    # Test a valid URL with http prefix
    url = 'http://www.example.com'
    assert Transformer.get_hostname_from_url(url) == 'www.example.com'

    # Test a valid URL with https prefix
    url = 'https://www.example.com'
    assert Transformer.get_hostname_from_url(url) == 'www.example.com'

    # Test a URL without the http(s) prefix
    url = 'www.example.com'
    assert Transformer.get_hostname_from_url(url) == 'NA'

    # Test an invalid URL
    url = 'invalid-url'
    assert Transformer.get_hostname_from_url(url) == 'NA'

    # Test an empty URL
    url = ''
    assert Transformer.get_hostname_from_url(url) == 'NA'

def test_get_domain_from_url():
    # Test a valid URL with http prefix
    url = 'http://www.example.com'
    assert Transformer.get_domain_from_url(url) == 'example.com'

    # Test a valid URL with https prefix
    url = 'https://www.example.com'
    assert Transformer.get_domain_from_url(url) == 'example.com'

    # Test a URL without the http(s) prefix
    url = 'www.example.com'
    assert Transformer.get_domain_from_url(url) == 'NA'

    # Test an invalid URL
    url = 'invalid-url'
    assert Transformer.get_domain_from_url(url) == 'NA'

    # Test an empty URL
    url = ''
    assert Transformer.get_domain_from_url(url) == 'NA'
