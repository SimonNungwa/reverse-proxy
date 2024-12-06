import httpx
import time

class Cache:
    def __init__(self):
        # Cache structure: {site_url: (status_code, timestamp)}
        self.cache = {}
        self.expiry_time = 300  # Cache expiry time in seconds (e.g., 5 minutes)

    def get(self, site):
        """Retrieve the cached status if valid."""
        if site in self.cache:
            status, timestamp = self.cache[site]
            if time.time() - timestamp < self.expiry_time:
                return status  # Return cached status
            else:
                del self.cache[site]  # Remove expired cache
        return None

    def set(self, site, status):
        """Store the status in the cache."""
        self.cache[site] = (status, time.time())


class HandleRequest:
    def __init__(self, site, cache):
        self.site = site
        self.cache = cache

    def check_status(self):
        # Check cache first
        cached_status = self.cache.get(self.site)
        if cached_status is not None:
            print("Cache hit!")
            return cached_status
        
        print("Cache miss. Fetching status...")
        # If not cached, fetch the status
        try:
            response = httpx.get(self.site)
            status_code = response.status_code
            # Cache the response
            self.cache.set(self.site, status_code)
            return status_code
        except httpx.RequestError as e:
            return f"An error occurred: {e}"


# Usage
print("Enter the site URL:")
site = input().strip()
cache_instance = Cache()
request_handler = HandleRequest(site, cache_instance)

result = request_handler.check_status()
print(f"Status Code: {result}")
