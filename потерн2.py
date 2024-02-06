# Target interface
class Target:
    def request(self):
        pass

# Adaptee (the class that needs to be adapted)
class Adaptee:
    def specific_request(self):
        print("Adaptee's specific request")

# Adapter
class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        print("Adapter's request")
        self.adaptee.specific_request()

# Client
def client_code(target):
    target.request()

# Usage
if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee)

    # Client code can work with Target interface
    client_code(adapter)
