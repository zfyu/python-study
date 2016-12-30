##IO编程
同步IO，异步IO(回调模式，轮询模式)  
本章的IO编程是同步模式。  
###文件读写
现代操作系统不允许普通程序直接操作磁盘，读写文件就是请求操作系统打开一个文件对象(文件描述符)，然后通过操作系统提供的接口从这个文件对象中读取数据，或者把数据写入这个文件对象。  
**读文件**  
f = open('file path/name','r')  
如果文件不存在open()函数会抛出IOError错误。  
调用read()一次读取文件全部内容，read(size),readline(),readlines()一次读取所有内容，并按行返回list。  
最后，f.close()  
为了保证无论是否出错都能正确关闭文件，使用try...finally来实现。  
也可使用with语句自动调用close()方法。  
with open(...) as f:  
　print(f.read)  
**file-like Object**  
像open()函数返回的这种有个read()方法的对象，在python中统称为file-like Object.除file外，还可以是内存的字节流、网络流、自定义流等。file-like Object不要求从特定类继承，只要写个read()方法就好。  
StringIO就是在内存中创建的file-like Object,常用作临时缓冲。  
读取UTF-8编码的文本文件。  
**二进制文件**  
要读取二进制文件，比如图片，视频，用'rb'模式打开文件即可。  
**字符编码**  
要读取非UTF-8编码的文本文件，要给open()函数传入encoding参数。  
open(...,encoding='gbk').  
有些编码不规范的文件，可能遇到UnicodeDecodeError，因为文本文件中夹杂了一些非法编码字符。遇到这种情况，open()函数还接收一个errors参数，表示遇到编码错误后，如何处理。最简单的就是直接忽略。  
f = open('file path/name','r',encoding='gbk',errors='ignore')  
**写文件**  
与读文件相似，调用open()函数时，传入标识符'w','wb'.  
f.write('test')  
f.close()  
反复调用write()来写入文件，调用f.close()来关闭文件。  
当我们写文件时，操作系统不是立刻把数据写入磁盘，而是放到内存缓存起来，空闲时候再慢慢写入。只有调用close()方法，系统才保证把没有写入的数据全部写入磁盘。未调用close()，可能只写一部分到磁盘，另一部分丢失。还是用with语句更保险。  
要写入特定编码的文本文件，给open()传入encoding参数。  
###StringIO和BytesIO
**StringIO**  
在内存中读写str.  
首先创建一个StringIO. from io import StringIO  
f= StringIO()  
f.write('test')  
f.getvalue()  
getvalue()方法用于获得写入后的str.  
要读取StringIO，可以用一个str初始化StringIO，然后像文件一样读取。  
**BytesIO**  
要操作二进制数据，使用BytesIO。  
from io import BytesIO  
f = BytesIO()  
f.write('中文'.encode('utf-8'))  
写入的是经过UTF-8编码的bytes。  
###操作文件和目录
python内置的os模块可以直接调用操纵系统提供的接口函数。  
os.name,os.uname()#uname()函数在windows上不提供。  
os.environ,操作系统的环境变量。  
要获取某个环境变量的值，可以调用os.environ.get('key').  
**操作文件和目录**  
操作文件和目录的一部分放在os模块中，一部分放在os.path模块中。  
查看、创建和删除目录：  
os.path.abspath('.')#查看当前目录的绝对路径  

os.path.join('path','newDir')#在某个目录下创建一个新目录，首先把新目录的完整路径表示出来。  
os.mkdir('path/newDir')#然后创建一个目录  

os.rmdir('path/newDir')#删除一个目录  

把两个路径合成一个时，通过os.path.join()函数，可以正确处理不同操作系统的路径分隔符。 / or \\   
要拆分路径时，通过os.path.split()函数，把一个路径拆分成两个部分，后一部分总是最后级别的目录或文件名。  
os.path.split('path/dir')  
os.path.splitext()可以直接让你得到文件的扩展名。  
 
**文件操作**  
os.rename('oldname','newname')  
os.remove('newname')  
os模块中不存在复制文件函数。但shutil模块提供了copyfile()函数。  

利用python的特性来过滤文件。  
列出当前目录下的所有目录：  
[x for x in os.listdir('.') if os.path.isdir(x)]  
要列出所有.py文件：  
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']  
###序列化
把变量从内存中变成可存储或传输的过程称之为序列化，在python中叫pickling。序列化后，可以把序列化后的内容写入磁盘，或通过网络传输到别的机器上。  
把变量内容从序列化的对象重新读到内存里称之为反序列化。unpickling.  
python提供了pickle模块实现序列化。  
import pickle  
pickle.dumps()方法把任意对象序列化成一个bytes,然后可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object.  
当我们把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。  
###JSON
如果我们要在不同编程语言之间传递对象，就必须把对象序列化成标准格式。序列化为JSON，JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。  
JSON表示的对象就是标准的Javascript语言的对象。  
python内置的json模块提供了完善的python对象到JSON格式的转换。  
import json
json.dumps(d),dumps()方法返回一个str，内容是标准的JSON，dump()方法直接把JSON写入一个file-like Object。  
要把JSON反序列化为python对象，用loads()或load()方法，前者把JSON字符串反序列化，后者从file-like Object中读取字符串并反序列化。  
JSON标准规定的编码是UTF-8，所以总能正确地在python的str与json字符串之间转换。  
**JSON进阶**  
序列化class，default参数就是把任意一个对象变成一个可序列为JSON的对象，为class专门写一个转换函数。  default=func1
反序列化，同理。object_hook=func2