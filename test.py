
class Hello:

    def __init__(self):
        self._x = None

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    x = property(get_x, set_x, "Property Name")

hello_world = Hello()
hello_world.x = 1

print(hello_world.x)
