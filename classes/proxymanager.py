class ProxyManager:
    def __init__(self):
        with open('proxies.txt') as proxy_file:
            self.proxies = proxy_file.readlines()
        self.index = 0

    def get_next_proxy(self):
        if self.index == len(self.proxies):
            self.index = 0
        return self.proxies[self.index]
