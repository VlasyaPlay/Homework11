import inspect


def introspection_info(obj):
    global attr
    obj_type = type(obj).__name__

    attributes = []
    methods = []

    for attr in dir(obj):

        if callable(getattr(obj, attr)):
            methods.append(attr)
        else:
            attributes.append(attr)

    obj_module = inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else 'builtin'

    is_instance = inspect.isclass(obj)

    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module,
        'is_class': is_instance
    }

    return info


class MyClass:
    def __init__(self, x):
        self.x = x

    def my_method(self):
        return self.x ** 2


number_info = MyClass(42)

class_info = introspection_info(number_info)
print(class_info)