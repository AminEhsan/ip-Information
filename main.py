from time import sleep
from requests import get


class IP:
    """A class to retrieve IP information."""

    __BASE_URL = 'http://ip-api.com/json'
    __PARAMS = {'fields': 'status,country,regionName,isp,mobile,proxy,hosting,query'}

    def information(self, proxies: dict) -> dict:
        """Fetch IP information."""
        counter = 0
        while True:
            counter += 1
            try:
                r = get(url=self.__BASE_URL, params=self.__PARAMS, proxies=proxies)
                assert (r.status_code == 200) and ('application/json' in r.headers['Content-Type']) and (r.json()['status'] == 'success')
                return r.json()
            except Exception as e:
                print(e)
                if counter >= 5:
                    print(f'Fetch IP information failed counter: {counter}')
                    raise e
                sleep(10)
