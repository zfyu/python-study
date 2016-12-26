##面向对象编程(Object Oriented Programming)
OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。  
在python中，所有数据类型都可视为对象，自定义的对象数据类型就是面向对象的类(class)概念。  
对象的方法(method)  
类(class)和实例(instance)  
数据封装，继承和多态是面向对象的三大特点。  
###类和实例
class Student(object):  
1、class后接类名，类名通常以大写字母开头，(object),表示，从哪个类继承下来。
2、可以自由的给一个实例变量绑定属性。  
3、类起到模板的作用，可以在创建实例的时候，把一些我们认为必须绑定的属性强制写进去。通过定义一个特殊的__init__方法，在创建实例时，把属性绑定。  
__init__方法的第一个参数永远是self,表示创建的实力本身。  
和普通函数相比，在类中定义的函数只有一点不同，第一个参数永远是实例变量self，并且，调用时，不用传递该参数。  
**数据封装**  
封装数据的函数和类本身相关联，我们称之为类的方法。  
数据和逻辑被“封装”，调用很简单，不用知道内部实现的细节。  
封装可以给类增加新的方法。  

类是创建实例的模板，而实例是一个个具体的对象。  
方法是与实例绑定的函数。  
和静态语言不同，python允许对实例变量绑定任何数据，对于两个实例变量，虽然它们属于同一个类的不同实例，但拥有的变量名称可能不同。  
###访问限制
要让类内部属性不被外部访问，可以在属性前加上两个下划线**\_\_**.变成一个私有变量(private)  
确保外部代码不能随意修改对象内部的状态，通过访问限制的保护，代码更加健壮。  
get_attribute(),set_attribute()  
在python中，变量名类似\_\_xxx\_\_,是特殊变量，可以直接访问，不是private变量。  
有时有一个下划线开头的实例变量名\_name，这样实例外部是可以访问，但约定俗成，视为私有变量，不随意访问。  

\_\_name,python解释器对外把\_\_name变量变成了\_Student\_\_name,所以，可以通过\_Student\_\_name来访问\_\_name变量。  
###继承和多态
子类(subclass),基类，父类，超类(base class,super class)  
当子类和父类存在相同方法时，子类方法覆盖父类的方法。 --**多态**  
在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类，但反过来就不行。  
“开闭”原则：对扩展开放，对修改封闭。  
**静态语言vs动态语言**  
动态语言的“鸭子类型”。不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。 
file-like object  
###获取对象信息
判断对象的类型  
1、**type(123)**  
判断基本数据类型，直接写：type(123) == int  
判断一个对象是否是函数：  
import types  
def fn():  
　pass  
type(fn) == types.FunctionType  
type(abs) == types.BuiltinFunctionType  
type(lambda x:x) == types.LambdaType  
type((x for x in range(10))) ==types.GeneratorType  
2、**使用isinstance()**  
并且可以判断一个变量是不是某些类型中的一种。  
isinstance([1,2,3],(list,tuple))  
3、**使用dir()**  
如果要获得一个对象的所有属性和方法，使用dir()函数。  
\_\_xxx\_\_的属性和方法在python中都是有特殊用途的，比如\_\_len\_\_方法返回长度。在python中调用len()函数试图获取一个对象的长度，实际上在len()函数内部，它自动调用该对象的\_\_len\_\_()方法。  
len('abc'),等价于'abc'.\_\_len\_\_().  
自己写的类，如果也要用len(myObj),就自己写一个\_\_len\_\_()方法。  
配合getattr()、setattr()、hasattr()，我们可以直接操作一个对象的状态。  
###实例属性和类属性
python是动态语言，根据类创建的实例可以任意绑定属性。  
给实例绑定属性，通过实例变量，或通过self变量。  
类属性，直接在class中定义属性。  
实例属性和类属性不要使用相同的名字，相同名称的实例属性将屏蔽类属性。当删除实例属性(del ins.attr)后，访问到的将是类属性。  
##面相对象高级编程
###使用\_\_slots\_\_
可以给实例绑定一个属性，也可以给实例绑定一个方法  
def func(self,tem):  
　self.tem = tem  
from types import MethodType  
s.func = MethodType(func,s)  
但给一个实例绑定的方法，对另一个实例不起作用。  
为了给所有实例都绑定方法，可以给class绑定方法。所有实例均可调用。  
**使用\_\_slots\_\_**  
限制实例的属性，只允许对Student实例添加name和age属性。  
class Student(object):  
　\_\_slots\_\_ = ('name','age')  
\_\_slots\_\_定义的属性仅对当前类实例起作用，对继承子类不起作用。  
###使用@property
既能检查属性参数，又可以用类似属性这样的简单方法来访问类变量。  
@property装饰器就是负责把一个方法变成属性调用的。  
把一个getter方法变成属性，只需要加上@property。此时，@property本身又创建了另一个装饰器@属性名.setter,负责把一个setter方法变成属性赋值。此时是可读性属性，如不定义@属性名.setter方法，就是一个只读属性。  
###多重继承
class Dog(Mammal,RunnableMixIn,CarnivorousMixIn):  
dog继承了三个父类(哺乳动物，runnable,肉食动物)。  
主线单一继承，dog继承自Mammal,混入额外的功能，同时继承Runnable，这种设计通常称为"MixIn"，为了更好的看出继承关系，改为RunnableMixIn.  
###定制类
**\_\_str\_\_**  
\_\_str\_\_()返回用户看到的字符串，\_\_repr\_\_()返回程序开发者看到的字符串。  
**\_\_iter\_\_**  
如果一个类想被用于for...in循环，就必须实现一个\_\_iter\_\_()方法，该方法返回一个迭代对象，然后python的for循环就会不断调用该迭代对象的\_\_next\_\_()方法拿到循环的下一个值，直到遇到StopIteration错误退出循环。  
**\_\_getitem\_\_**  
实现像list那样按照下标取出元素，需要实现\_\_getitem\_\_()方法。  
通过对传入参数的判断，可以实现切片等。  
还有\_\_setitem\_\_()方法，把对象视作list或dict来对集合赋值。  
还有\_\_delitem\_\_()方法，用于删除某个元素。  
**\_\_getattr\_\_**  
动态返回一个属性，当调用不存在的属性时，python解释器会试图调用\_\_getattr\_\_(self,'attr')来尝试获得属性。也可返回函数。  
作用：针对完全动态的情况作调用。  
**\_\_call\_\_**  
一个对象实例有自己的属性和方法，调用实例方法时，用instance.method()来调用。  
任何类，只需要定义一个\_\_call\_\_()方法，就可以直接对实例进行调用。  
判断一个函数能否被调用，能被调用的对象就是一个Callable对象。  
callable([1,2,3])  
###使用枚举类
为枚举类型定义一个class类型，每个常量都是class的唯一实例，python提供Enum类。  
from enum import Enum  
即可以用成员名称引用枚举变量，又可以直接根据value值获取枚举变量。  
###使用元类
**type()**  
动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。  
class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。  
type()函数既可以返回一个对象的类型，又可以创建出新的类型。通过type()创建Hello类。  
def fn(self,name='world'):# 定义函数  
　print('hello %s.'%name)  
  
Hello = type('Hello',(object,),dict(hello=fn))#创建Hello class  
h=Hello()  
h.hello()  
创建一个class对象，type()函数依次传入三个参数：  
1、class的名称  
2、继承的父类集合，支持多重继承。如果只有一个父类，注意tuple的单元素写法  
3、class的方法名称与函数绑定。  
**metaclass**  
先定义类，然后创建出实例。  
先定义metaclass，就可以创建类，最后创建实例。  
(此部分暂时跳过)


