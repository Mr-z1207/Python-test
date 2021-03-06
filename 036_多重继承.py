# # 假设我们要实现以下4种动物
# # Dog - 狗狗
# # Bat - 蝙蝠
# # Parrot - 鹦鹉
# # Ostrich - 鸵鸟
# 如果按照哺乳动物和鸟类归类，我们可以设计出这样的类的层次：

#                 ┌───────────────┐
#                 │    Animal     │
#                 └───────────────┘
#                         │
#            ┌────────────┴────────────┐
#            │                         │
#            ▼                         ▼
#     ┌─────────────┐           ┌─────────────┐
#     │   Mammal    │           │    Bird     │
#     └─────────────┘           └─────────────┘
#            │                         │
#      ┌─────┴──────┐            ┌─────┴──────┐
#      │            │            │            │
#      ▼            ▼            ▼            ▼
# ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
# │   Dog   │  │   Bat   │  │ Parrot  │  │ Ostrich │
# └─────────┘  └─────────┘  └─────────┘  └─────────┘
# 但是如果按照“能跑”和“能飞”来归类，我们就应该设计出这样的类的层次：

#                 ┌───────────────┐
#                 │    Animal     │
#                 └───────────────┘
#                         │
#            ┌────────────┴────────────┐
#            │                         │
#            ▼                         ▼
#     ┌─────────────┐           ┌─────────────┐
#     │  Runnable   │           │   Flyable   │
#     └─────────────┘           └─────────────┘
#            │                         │
#      ┌─────┴──────┐            ┌─────┴──────┐
#      │            │            │            │
#      ▼            ▼            ▼            ▼
# ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
# │   Dog   │  │ Ostrich │  │ Parrot  │  │   Bat   │
# └─────────┘  └─────────┘  └─────────┘  └─────────┘
# 如果要把上面的两种分类都包含进来，我们就得设计更多的层次：

# 哺乳类：能跑的哺乳类，能飞的哺乳类；
# 鸟类：能跑的鸟类，能飞的鸟类。
# 这么一来，类的层次就复杂了：

#                 ┌───────────────┐
#                 │    Animal     │
#                 └───────────────┘
#                         │
#            ┌────────────┴────────────┐
#            │                         │
#            ▼                         ▼
#     ┌─────────────┐           ┌─────────────┐
#     │   Mammal    │           │    Bird     │
#     └─────────────┘           └─────────────┘
#            │                         │
#      ┌─────┴──────┐            ┌─────┴──────┐
#      │            │            │            │
#      ▼            ▼            ▼            ▼
# ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
# │  MRun   │  │  MFly   │  │  BRun   │  │  BFly   │
# └─────────┘  └─────────┘  └─────────┘  └─────────┘
#      │            │            │            │
#      │            │            │            │
#      ▼            ▼            ▼            ▼
# ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
# │   Dog   │  │   Bat   │  │ Ostrich │  │ Parrot  │
# └─────────┘  └─────────┘  └─────────┘  └─────────┘
# 如果要再增加“宠物类”和“非宠物类”，这么搞下去，
# 类的数量会呈指数增长，很明显这样设计是不行的


# 正确的做法是采用多重继承。首先，主要的类层次仍按照哺乳类和鸟类设计
class Animal:
    pass


# 大类（哺乳类鸟类）:
class mammal(Animal):
    pass


class Bird(Animal):
    pass


# # 各种动物:
# class Dog(mammal):
#     pass


# class Bat(mammal):
#     pass


# class Ostrich(Bird):
#     pass


# class Parrot(Bird):
#     pass


# 现在，我们要给动物再加上Runnable和Flyable的功能
class Runnable(object):
    def run(self):
        print('Running...')


class Flyable(object):
    def fly(self):
        print('Flying...')


# 各种动物:
class Dog(mammal, Runnable):
    pass


class Bat(mammal, Flyable):
    pass

# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。
# 但是，如果需要“混入”额外的功能，通过多重继承就可以实现，
# 比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。

# 为了更好地看出继承关系，我们把Runnable和Flyable改为RunnableMixIn和FlyableMixIn。
# 类似的，你还可以定义出肉食动物CarnivorousMixIn和植食动物HerbivoresMixIn，
# 让某个动物同时拥有好几个MixIn：
