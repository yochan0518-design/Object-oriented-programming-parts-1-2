class robot:
    def __init__(self, name, model, purpose):
       self.name = name
       self.model = model
       self.purpose = purpose

    def introduce_self(self):
        print(f"Hello World! i am {self.name}.")
        print(f"My purpose is :{self.purpose} I am a {self.model}.")

my_robot = robot( name = "odi", model = "Optic 7", purpose = "I am a robot, made to last and help othe with my name, as it stands for Object Data Interface, i can also down and upload my versions of advanced code in any regions of syntax")

my_robot.introduce_self()