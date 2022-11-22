class Pizza:
    """
    Класс описывает пиццу
    """
    def __init__(self, recipe: dict, size: str = 'L', emoji: str = '🍕'):
        """
        :param recipe: ингредиенты пиццы;
        :param size: размер пиццы;
        :param emoji: по умолчанию каждому типу пиццы назначен свой смайлик.
        """
        self.size = size
        self.recipe = recipe
        self.emoji = emoji

    def __eq__(self, other) -> bool:
        """
        Магический метод, возвращает True, если две пиццы одинаковы, иначе - False
        """
        return (self.size == other.size and
                self.recipe == other.recipe and
                self.__class__ == other.__class__)

    def dict(self) -> dict:
        """
        :return: возвращает ингредиенты в виде словаря.
        """
        return self.recipe

    def __repr__(self) -> str:
        """
        Магический метод, возвращает информацию о пицце: название, смайлик: ингредиенты
        """
        ingredients = ', '.join(list(self.dict().values()))
        output = f'- {type(self).__name__} {self.emoji}: {ingredients}'
        return output

    @staticmethod
    def menu() -> list:
        """
        :return: список подклассов класса пиццы - то есть видов пицц.
        """
        return Pizza.__subclasses__()

    @staticmethod
    def order(ordered_pizza: str) -> type:
        """
        По текстовому имени возвращает подкласс (то есть вид) пиццы. Имя может быть не с большой буквы.
        Если по имени ничего не нашлось, возвращается Маргарита.
        :param ordered_pizza:
        :return:
        """
        for pizza_item in Pizza.menu():
            if pizza_item.__name__.lower() == ordered_pizza.lower():
                return pizza_item
        else:
            print('Такого у нас нет! Лучше попробуйте Маргариту!')
            return Margherita


class Margherita(Pizza):
    """
    Класс описывает пиццу Маргарита
    """
    def __init__(self, recipe: dict = None, size: str = 'L', emoji: str = '🧀'):
        if recipe is None:
            recipe = {'sauce': 'tomato sauce',
                      'cheese': 'mozzarella',
                      'vegs': 'tomatoes'
                      }
        super().__init__(recipe, size, emoji)


class Hawaiian(Pizza):
    """
    Класс описывает Гавайскую пиццу
    """
    def __init__(self, recipe: dict = None, size: str = 'L', emoji: str = '🍍'):
        if recipe is None:
            recipe = {'sauce': 'tomato sauce',
                      'cheese': 'mozzarella',
                      'meet': 'chicken',
                      'vegs': 'pineapples'
                      }
        super().__init__(recipe, size, emoji)


class Pepperoni(Pizza):
    """
    Класс описывает пиццу Пепперони
    """

    def __init__(self, recipe: dict = None, size: str = 'L', emoji: str = '🍕'):
        if recipe is None:
            recipe = {'sauce': 'tomato sauce',
                      'cheese': 'mozzarella',
                      'meet': 'pepperoni',
                      }
        super().__init__(recipe, size, emoji)
