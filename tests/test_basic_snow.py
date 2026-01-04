import pytest
from vibium import browser_sync


def test_simple_pass():    
    vibe = browser_sync.launch()
    vibe.go("https://dev300645.service-now.com/")

    vibe.find("all").click()
    vibe.find("all").type("admin")

    vibe.quit()


