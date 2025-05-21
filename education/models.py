from django.db import models

class EducationProgram(models.Model):
    student_name = models.CharField("ФИО студента", max_length=100)
    program_name = models.CharField("Название программы", max_length=100)
    year = models.PositiveIntegerField("Год поступления")
    score = models.DecimalField("Балл", max_digits=5, decimal_places=2)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Программа"
        verbose_name_plural = "Программы"

    def __str__(self):
        return f"{self.student_name} ({self.program_name})"