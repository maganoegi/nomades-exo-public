
import abc

class Test( abc.ABC ):
    @abc.abstractmethod
    def launch(self):
        """ this is a docstring """

    def default_whatever(self):
        print("whatever by default")

class Unittest( Test ):
    def __init__(self, a):
        self.a = a

    def say_hi(self):
        print("hi")

    def launch(self):
        print("je fais des tests unitaires")

    def of(class_data: dict):
        ...

class ScenarioTest( Test ):
    def say_bye(self):
        print("bye")

    def launch(self):
        print("je fais des tests scenario")


if __name__ == '__main__':
    ut = Unittest(1)
    ut.say_hi()
    print(dir(ut))
    # ut.__class__ = ScenarioTest
    # ut.say_hi()
