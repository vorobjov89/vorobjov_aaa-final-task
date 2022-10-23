import pizza
import click
from random import randint
from string import Template


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.option('--xl', default=False, is_flag=True)
@click.argument('ordered_pizza', nargs=1)
def order(ordered_pizza: str, delivery: bool, xl: bool) -> object:
    """
    Заказ пиццы
    """
    if xl:  # Размер пиццы.
        size = 'XL'
    else:
        size = 'L'

    new_pizza = (pizza.Pizza.order(ordered_pizza))(size=size)  # Возвращается класс, здесь создаем его экземпляр.
    to_bake(new_pizza)

    if delivery:
        to_deliver(new_pizza)
    else:
        to_pick_up(new_pizza)

    return new_pizza


def log(template: str):
    """
    Декоратор выводит сообщение при вызове декорируемой функции по шаблону.

    template: шаблон сообщения, которое выводится при вызове декорируемой функции.
    """
    def decorator(func):
        def wrapper(*args):
            func(*args)
            time = randint(1, 10)
            t = Template(template) # Пользуемся Template, чтобы придать функции шаблон сообщения.
            data = dict(time=time)
            print(t.substitute(data))
            return func(*args)
        return wrapper
    return decorator


@log(' 🛵  Забрали за $time с!')
def to_deliver(pizza_to_deliver):
    """
    Доставляем пиццу
    """
    return pizza_to_deliver


@log('👨‍🍳Приготовили за $time с!')
def to_bake(pizza_to_bake):
    """
    Печем пиццу
    """
    return pizza_to_bake


@log(' 🏠  Забрали за $time с!')
def to_pick_up(pizza_to_pick_up):
    """
    Самовывоз пиццы
    """
    return pizza_to_pick_up


@cli.command()
def menu():
    """
    Выводит меню
    """
    for pizza_item in pizza.Pizza.menu():
        print(pizza_item())


if __name__ == '__main__':
    cli()
