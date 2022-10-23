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
        return self.size == other.size and self.recipe == other.recipe

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
        output = f'- {self.__class__.__name__} {self.emoji}: {ingredients}'
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
            if pizza_item.__name__ == ordered_pizza or pizza_item.__name__.lower() == ordered_pizza:
                return pizza_item
        else:
            print('Такого у нас нет! Лучше попробуйте Маргариту!')
            return Margherita


class Margherita(Pizza):
    """
    Класс описывает пиццу Маргарита
    """
    def __init__(self, size: str = 'L'):
        Pizza.__init__(self,
                       {'sauce': 'tomato sauce',
                        'cheese': 'mozzarella',
                        'vegs': 'tomatoes'
                        },
                       size,
                       '🧀',)


class Hawaiian(Pizza):
    """
    Класс описывает Гавайскую пиццу
    """
    def __init__(self, size: str = 'L'):
        Pizza.__init__(self,
                       {'sauce': 'tomato sauce',
                        'cheese': 'mozzarella',
                        'meet': 'chicken',
                        'vegs': 'pineapples'
                        },
                       size,
                       '🍍',)


class Pepperoni(Pizza):
    """
    Класс описывает пиццу Пепперони
    """
    def __init__(self, size: str = 'L'):
        Pizza.__init__(self,
                       {'sauce': 'tomato sauce',
                        'cheese': 'mozzarella',
                        'meet': 'pepperoni',
                        },
                       size,
                       '🍕',)
