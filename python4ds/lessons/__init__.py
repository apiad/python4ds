from . import lesson_00_introduction, lesson_01_variables


lessons = { f"Lesson {i} - {l.title()}": l for i,l in enumerate([
    lesson_00_introduction,
    lesson_01_variables
]) }


__all__ = ['lessons']
