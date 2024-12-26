from dataclasses import dataclass
from abstract_class_interfaces import Course

@dataclass(order=True, frozen=False, init=True, repr=True, kw_only=False)
class EdMedCourse(Course):
    """
    Class implemented with dataclass decorator and inherits Course Interface
    """
    # instance variables
    course_name: str
    course_duration: int
    course_genre: str
    course_cost: int

    # class variables which is private
    _platform: str = 'Ed-med'
    _courses: list[str] = None

    def __post_init__(self) -> None:
        """
        Trigger post object initialization
        Check the cost, if it is 0 then it makes it to 1000 as default
        :return:
        """
        if self.course_cost == 0:
            self.course_cost = 1000

    @classmethod
    def platform(cls) -> None:
        """
        It is a class method indicated by the decorator
        :return: None
        """
        return cls._platform

    @classmethod
    def list_course(cls) -> None:
        """
        We should implement this because we're inheriting from Course class (Interface)
        :return: None
        """
        for index, course in enumerate(cls._courses, start=1):
            print(f'{index}. {course}')

    @classmethod
    def add_courses(cls, new_course: str) -> None:
        """
        Class method represented by decorator
        :param new_course: Adding courses to the class
        :return:
        """
        if new_course is not None:
            cls._courses.append(new_course)

if __name__ == '__main__':
    print(EdMedCourse.welcome_message())
    course_obj = EdMedCourse('Fast Booming World', 2, 'Tech', 0)
    print(course_obj.course_cost)
