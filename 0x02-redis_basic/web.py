import requests
import redis

# Initialize Redis client
r = redis.StrictRedis(host='localhost', port=6379, db=0)

def cache_page(expiration: int):
    """Decorator to cache the result of a function."""
    def decorator(func):
        def wrapper(url: str):
            # Track access count
            access_key = f"count:{url}"
            r.incr(access_key)  # Increment the access count
            
            # Check if the cached value exists
            cached_content = r.get(url)
            if cached_content:
                return cached_content.decode('utf-8')

            # If not cached, call the original function to fetch the page
            content = func(url)

            # Cache the content with an expiration time
            r.setex(url, expiration, content)

            return content
        return wrapper
    return decorator

@cache_page(10)  # Cache for 10 seconds
def get_page(url: str) -> str:
    """Fetches the HTML content of a given URL."""
    response = requests.get(url)
    return response.text

# Example usage
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/10/url/http://example.com"
    print(get_page(url))  # This will fetch the page and cache it
    print(get_page(url))  # This will return the cached content

