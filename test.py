# 定义一个空类
class Student:
    # 暂时没想好类中的内容，用pass来跳过
    pass


class PythonStudent:
    name = None
    age = 18
    course = "Python"

    # 类中的方法
    # 1.def do_homework的缩进注意
    # 2.系统默认self参数
    def do_homework(self):
        print("在写作业")
        return None


# 实例化一个对象
student1 = PythonStudent()
print(student1.name)
print(student1.age)
student1.do_homework()
