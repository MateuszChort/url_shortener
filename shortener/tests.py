import pytest
from rest_framework.test import APIClient
from django.urls import reverse


@pytest.fixture
def client():
    return APIClient()


@pytest.mark.django_db
def test_create_short_url(client, mocker):
    mocker.patch("shortener.utils.generate_code", return_value="abc123")
    url = reverse("shorten-url")
    response = client.post(
        url, {"original_url": "http://example.com/some_long_url/this_is_a_test"}
    )
    assert response.status_code == 200
    assert "short_url" in response.data
    assert response.data["short_url"].endswith("/short/abc123")


@pytest.mark.django_db
def test_expand_short_url(client, mocker):
    mocker.patch("shortener.utils.generate_code", return_value="abc123")
    url = reverse("shorten-url")
    post_resp = client.post(
        url, {"original_url": "http://example.com/some_long_url/this_is_a_test"}
    )
    code = post_resp.data["short_url"].split("/")[-1]
    expand_url = reverse("expand-url", args=[code])
    expand_resp = client.get(expand_url)
    assert expand_resp.status_code == 200
    assert (
        expand_resp.data["original_url"]
        == "http://example.com/some_long_url/this_is_a_test"
    )
