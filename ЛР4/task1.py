class Animal:
    """
    Базовый класс, представляющий животное
    """
    def __init__(self, name: str, age: int, species: str) -> None:
        """
        Аргументы:
            name: имя животного
            age: возраст животного
            species: вид животного (например, "млекопитающее")
        """
        self.name = name
        self._age = age          # инкапсулируем возраст, чтобы контролировать доступ
        self._species = species   # инкапсулируем вид, так как он не должен меняться после создания

    def __str__(self) -> str:
        """
        Возвращает удобочитаемое строковое представление животного
        """
        return f"{self.name} ({self._species}), {self._age} лет"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление для отладки
        """
        return f"Animal(name='{self.name}', age={self._age}, species='{self._species}')"

    def make_sound(self) -> str:
        """
        Возвращает строку со звуком, который издаёт животное
        Базовый метод возвращает общий звук
        """
        return "Издаёт какой-то звук"

    def get_age(self) -> int:
        """
        Геттер для защищённого атрибута _age
        """
        return self._age


class Dog(Animal):
    """
    Дочерний класс, представляющий собаку. Наследуется от Animal.
    """
    def __init__(self, name: str, age: int, breed: str) -> None:
        """
        Аргументы:
            name: имя собаки
            age: возраст собаки
            breed: порода собаки
        """
        super().__init__(name, age, species="собака")
        self._breed = breed   # инкапсулируем породу, так как она не должна меняться после создания

    def __str__(self) -> str:
        """
        Перегруженный метод. Возвращает строку с именем, породой и возрастом
        """
        return f"{self.name} (порода {self._breed}), {self._age} лет"

    def __repr__(self) -> str:
        """
        Перегруженный метод. Возвращает формальное представление для Dog
        """
        return f"Dog(name='{self.name}', age={self._age}, breed='{self._breed}')"

    def make_sound(self) -> str:
        """
        Причина перегрузки: собаки издают специфический звук, отличный от общего
        """
        return "Гав"

if __name__ == "__main__":
    # Write your solution here
    pass
