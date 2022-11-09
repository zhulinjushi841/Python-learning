<!--
 * @Author: Jerome 841682441@qq.com
 * @Date: 2022-11-03 17:52:46
 * @LastEditors: Jerome 841682441@qq.com
 * @LastEditTime: 2022-11-09 16:11:21
 * @FilePath: \Python-learning\异常\with关键字及上下文管理.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
#### with关键字
在Python中，with关键字用于异常处理，封装了try...except...finally编码范式，提高了易用性。
wth语句使得代码更加清晰，更具可读性，并简化了文件流等公共资源的管理。

在处理文件对象时，使用with关键字是一种很好的做法。
对于系统资源比如文件、数据库连接、socket而言，应用程序打开这些资源并执行完业务逻辑之后，必须做的一件事就是关闭(断开)该资源。

下面是几种正确关闭一个文件的方式:<br>
__1.普通版__

    def m1():
        f = open("output.txt","w")
        f.write("python")
        f.close()

这样写有一个潜在的问题，如果在调用write的过程中，出现了异常而导致后续代码无法继续执行，close方法就无法被正常调用，因此系统分配的资源就会一直被该程序占用而不会释放。

为了改进代码，下面展示另一种打开方式:<br>
__2.进阶版__

    def m2():
    f = open("output.txt", "w")
    try:
        f.write("python")
    except IOError:
        print("error while writing files")
    finally:
        f.close()

改进版程序时对可能发生异常的代码进行try捕获，使用try/finally语句，该语句表示如果在try代码块中程序出现了问题，后续代码就不再执行，而直接跳转到except代码块。而无论如何， finally块的代码都会被执行。因此，只需要将close放在finally代码中，文件就一定会关闭。

__3.高级版__

    def m3():
        with open("output.txt", "r") as f:
            f.write("python)

一种更加间接、优雅的方式就是使用with关键字。open方法的返回值赋给变量f，当离开with代码块的时候，系统会自动调用f.close()方法，with的作用和使用try/finally语句是一样的。

__上下文管理__ <br>
with语句实质上式一个上下文管理器，with语句后的对象都会有__enter__()和__exit__()方法。
在进入上下文的时候，会自动调用__enter__()方法，程序正常执行完成，或者出现异常中断的时候，都会调用__exit__()方法。

    class MyContext(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def __enter__(self):
            print('调用了entert方法')
            return self
        
        def test(self):
            1 / 0
            print(self.name + '调用了test方法')
        
        def __exit__(self):
            print('调用了exit方法')
            print(exc_type, exc_val, exc_tb)
    
    with MyContext('zhangsan',18) as context:
        context.test()

执行结果:
![pic1](../pics/屏幕截图%202022-11-08%20210231.png)


