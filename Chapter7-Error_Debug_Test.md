##错误、调试和测试
###错误处理
try...except...finally...  
由不同的except语句块处理不同类型的错误。  
在except语句块后加一个else，当没有发生错误，会自动执行else语句。  
所有错误类型都继承自BaseException。  
**调用堆栈**  
如果错误没有被捕获，它就会一直往上抛，最后被python解释器捕获，打印一个错误信息，然后程序退出。  
**记录错误**  
捕获错误，打印错误堆栈，分析错误原因，让程序继续执行下去。  
python内置的logging模块可以容易的记录错误信息。  
**抛出错误**  
错误是class，捕获错误就是捕获该class的一个实例。  
根据需要，定义一个错误的class，选择好继承关系，然后用raise语句抛出一个错误实例。  
尽量选择python内置的错误类型。  
raise语句如果不带参数，就会把当前错误原样抛出。在except中raise一个Error，可以把一种类型的错误转化成另一种。应有合理的转换逻辑。   
###调试
1、print()  
2、断言，凡是需要用print()辅助查看的地方，都可用断言(assert)来替代。  
assert n!=0,'n is zero'  
assert的意思是，表达式n!=0,应该是True。  
如果断言失败，assert语句本身就会抛出AssertionError。  
在启动Python解释器时，可用-O参数关闭assert，关闭后，把所有的assert语句当成pass。  
3、logging  
把print()替换为logging，logging不会抛出错误，而且可以输出到文件。  
允许指定记录信息的级别，debug，info，warning，error级别。  
import logging  
logging.basicConfig(level=logging.INFO)  
logging.info('n = %d' %n)  
4、pdb  
启动python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。  
启动：python -m pdb test.py  
继续输入命令：  
l:查看代码  
n:单步执行代码  
p 变量名：查看变量  
q:结束调试，退出程序。  
**pdb.set_trace()**  
只需要import pdb  
在可能出错的语句前，放一个pdb.set_trace(),就可设置一个断点。  
运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用p查看变量，或用c继续执行。  
5、IDE
支持调试功能的IDE，PyCharm,Eclipse加上pydev插件。  
###单元测试
测试驱动开发(TDD:Test-Driven Development)  
单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。  
以测试为驱动的开发模式最大的好处就是确保一个程序模块的行为符合我们设计的测试用例，在将来修改时，可以极大程度地保证该模块行为仍是正确的。  
为编写测试，引入python自带的unittest模块。  
编写一个测试类，从unittest.TestCase继承。  
对每一类测试写一个test_xxx()方法，由于unittest.TestCase提供了很多内置的判断条件，我们只需要调用这些方法就可以断言输出是否是我们所期望的。  
常用断言：  
assertEqual(): self.assertEqual(abs(-1),1)#断言函数返回的结果与1相等。  
期待抛出指定类型的Error：  
with self.assertRaises(KeyError):  
　value = d['empty']  
而通过d.empty访问不存在的key时，我们期待抛出AttributeError。  
**运行单元测试**  
1、在xx\_test.py最后加上两行代码：  
if \_\_name\_\_ == '\_\_main\_\_':  
　unittest.main()  
这样可以把xx\_test.py当作正常python脚本运行。  
2、在命令行通过参数 -m unittest直接运行单元测试。(推荐，一个批量运行很多单元测试)  
**setUp与tearDown**  
在单元测试中编写两个特殊的setUp()和tearDown()方法，这两个方法会分别在每调用一个测试方法的前后分别被执行。  
小结：  
单元测试可以有效地测试某个程序模块的行为。  
单元测试的测试用例需要覆盖常用的输入组合、边界条件和异常。  
单元测试代码要简单。  
###文档测试
自动执行写在注释中的这些代码。  
python内置的文档测试(doctest)模块可以直接提取注释中的代码并执行测试。  
只有测试异常时，可以用...表示中间的一大段输出。注意>>>后的空格，Traceback后的空格。  
在测试python脚本的最后加上：  
if \_\_name\_\_ == '\_\_main\_\_':  
　import doctest  
　doctest.testmod()  
当模块正常导入时，doctest不会被执行，只有在命令行直接运行时，才执行doctest。  


