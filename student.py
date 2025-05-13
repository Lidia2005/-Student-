import uuid

class Uchashchijsya:
    kolichestvo_uchashchikhsya = 0  # Счётчик всех студентов

    def __init__(self, fio, vozrast):
        self.identifikator = str(uuid.uuid4())  # Уникальный ID
        self.fio = fio
        self.vozrast = vozrast
        self.predmety = {}  # Хранилище предметов и оценок
        self.srednyaya_ocenka = 0
        Uchashchijsya.kolichestvo_uchashchikhsya += 1

    def dobavit_predmet(self, predmet, ocenka):
        """Добавляет предмет и оценку к нему"""
        self.predmety[predmet] = ocenka
        self.obnovit_srednyuyu_ocenku()

    def obnovit_srednyuyu_ocenku(self):
        """Перерасчёт средней оценки"""
        if self.predmety:
            self.srednyaya_ocenka = sum(self.predmety.values()) / len(self.predmety)

    def pokazat_informaciyu(self):
        """Отображает данные об учащемся"""
        print("\n📘 Информация об учащемся:")
        print(f"🆔 ID: {self.identifikator}")
        print(f"👤 ФИО: {self.fio}")
        print(f"🎂 Возраст: {self.vozrast} лет")
        print(f"📊 Средняя оценка: {self.srednyaya_ocenka:.2f}")
        print("📚 Оценки по предметам:")
        for predmet, ocenka in self.predmety.items():
            print(f"   - {predmet}: {ocenka}")
        print("═" * 40)

    def uroven_uspevaemosti(self):
        """Оценка по уровню успеваемости"""
        if self.srednyaya_ocenka > 8:
            return "🌟 Отлично"
        elif 6 <= self.srednyaya_ocenka <= 8:
            return "✅ Хорошо"
        elif 4 <= self.srednyaya_ocenka < 6:
            return "⚠️ Удовлетворительно"
        else:
            return "❌ Неудовлетворительно"

    def sravnit_s(self, drugoj):
        """Сравнение с другим учащимся"""
        if self.srednyaya_ocenka > drugoj.srednyaya_ocenka:
            return f"{self.fio} показывает лучшие результаты, чем {drugoj.fio}"
        elif self.srednyaya_ocenka < drugoj.srednyaya_ocenka:
            return f"{drugoj.fio} показывает лучшие результаты, чем {self.fio}"
        else:
            return f"{self.fio} и {drugoj.fio} имеют одинаковый уровень"

    def povysit_ocenki(self, pribavka):
        """Повышает все оценки на указанное значение (максимум 10)"""
        for predmet in self.predmety:
            self.predmety[predmet] = min(self.predmety[predmet] + pribavka, 10)
        self.obnovit_srednyuyu_ocenku()

    @staticmethod
    def obshchee_kolichestvo():
        """Показывает общее количество студентов"""
        return Uchashchijsya.kolichestvo_uchashchikhsya

# ========== Пример использования ==========

uch1 = Uchashchijsya("Алексей Сидоров", 21)
uch1.dobavit_predmet("Информатика", 7)
uch1.dobavit_predmet("История", 8)

uch2 = Uchashchijsya("Ольга Смирнова", 20)
uch2.dobavit_predmet("Информатика", 9)
uch2.dobavit_predmet("История", 6)

uch1.pokazat_informaciyu()
uch2.pokazat_informaciyu()

# Сравнение
print("\n📈 Сравнение:")
print(uch1.sravnit_s(uch2))

# Повышение оценок
uch1.povysit_ocenki(1)
print("\n🔧 После повышения оценок:")
uch1.pokazat_informaciyu()

# Общее количество
print(f"\n👥 Всего студентов: {Uchashchijsya.obshchee_kolichestvo()}")

