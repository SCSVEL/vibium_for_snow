import pytest
from vibium import browser_sync


def test_simple_pass():
    from vibium import browser_sync
    import os
    from dotenv import load_dotenv

    load_dotenv()    
    
    vibe = browser_sync.launch()
    vibe.go(os.getenv("SNOW_URL"))

    vibe.find("user name").type(os.getenv("SNOW_USERNAME"))
    vibe.find("password").type(os.getenv("SNOW_PASSWORD"))
    vibe.find("login").click()    

    vibe.quit()