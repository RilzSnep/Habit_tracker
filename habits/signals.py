from django.db.models.signals import post_save
from django.dispatch import receiver
from habits.models import Habit
from habits.tasks import send_telegram_reminder
from datetime import datetime


@receiver(post_save, sender=Habit)
def schedule_habit_reminder(sender, instance, created, **kwargs):
    if created:
        now = datetime.now()
        # Преобразуем строку времени в объект time
        habit_time = datetime.strptime(str(instance.time), '%H:%M:%S').time()
        # Создаем полные datetime объекты для вычисления разницы
        current_datetime = datetime.combine(datetime.today(), now.time())
        habit_datetime = datetime.combine(datetime.today(), habit_time)
        delay = (habit_datetime - current_datetime).total_seconds()

        print(f"Текущее время: {now.time()}, Время привычки: {habit_time}, Задержка: {delay} секунд")
        if delay > 0:
            send_telegram_reminder.apply_async(args=[instance.id], countdown=delay)
        else:
            print("Время привычки уже прошло, уведомление не запланировано")
 
