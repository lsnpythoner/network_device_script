# 网络设备脚本
《网络设备脚本》的目标是以相同的代码以各种方式来控制不同的网络设备。

基本功能：
* 支持命令行控制网络设备（模拟人工敲命令）
* 支持网页控制网络设备（模拟人工点网页）

未来的设计目标：
* 支持软件定义网络
* 以其他方式控制网络设备

项目依赖项：
* [乘风龙王的代码库(python)](https://github.com/cflw/cflw_py)
* paramiko（安全外壳连接到网络设备时需要）
* pyserial（串口连接到网络设备时需要）
* pywin32（命名管道连接到网络设备时需要）
* selenium（网页控制网络设备时需要）
* pillow（网页控制网络设备时需要）

### 文章
* [用python编写控制网络设备的自动化脚本1：框架设计](https://zhuanlan.zhihu.com/p/53641620) \[知乎\]
* [用python编写控制网络设备的自动化脚本2：显示](https://zhuanlan.zhihu.com/p/56108138) \[知乎\]
* [用python编写控制网络设备的自动化脚本3：启动](https://zhuanlan.zhihu.com/p/56833809) \[知乎\]
* [用python编写控制网络设备的自动化脚本4：接口](https://zhuanlan.zhihu.com/p/59428605) \[知乎\]
* [用python编写控制网络设备的自动化脚本5：访问控制列表](https://zhuanlan.zhihu.com/p/63076652) \[知乎\]
* [用python编写控制网络设备的自动化脚本6：框架设计2](https://zhuanlan.zhihu.com/p/67650697) \[知乎\]
* [用python编写控制网络设备的自动化脚本7：跳板（远程登录）](https://zhuanlan.zhihu.com/p/83475460) \[知乎\]

## 内容包含
《网络设备脚本》支持的可以控制的**网络设备**的品牌有：

|↓品牌 \ 控制方式→|命令行<br>（CLI）|网页<br>（Web）|
|-|:-:|:-:|
|**思科**（Cisco）|√|√|
|**华为**（Huawei）|√||
|**华三**（H3C）|√||
|**中兴**（ZTE）|√||
|**锐捷**（Ruijie）|√||
|**迈普**（Maipu）|√||
|**博达**（BDCOM）|√||
|**浪潮**（Inspur）|√||
|**普联**（TP-Link）||√|
|**水星**（Mercury）||√|

可以控制的**安全设备**的品牌有：

|↓品牌 \ 控制方式→|命令行<br>（CLI）|网页<br>（Web）|
|-|:-:|:-:|
|**深信服**（Sangfor）||√|

对不同品牌不同型号设备的支持程度取决于有没有模拟器或者我能否拿到真机做实验。有时候没法做实验，很多代码写出来没法验证是否可用。

## 快速入门演示
```python
import cflw代码库py.cflw网络连接_安全外壳 as 安全外壳
import 网络设备脚本 as 脚本
import 网络设备脚本.思科 as 思科
def main():
	#第一步: 创建连接
	v连接 = 安全外壳.C安全外壳2("10.0.0.1", a用户名 = "asdf", a密码 = "1234")	#使用SSH连接到10.0.0.1

	#第二步: 创建设备
	v设备 = 思科.f创建设备(v连接, 思科.E型号.c7200, 15.0)	#指定型号思科c7200, 系统版本15.0

	#第三步: 创建用户模式
	v用户模式 = v设备.f模式_用户模式()	#进入用户模式
	v用户模式.f登录()	#检测状态并进入用户模式

	#第四步: 进入特定模式修改配置
	v全局配置 = v用户模式.f模式_全局配置()	#进入全局配置模式
	v接口配置 = v全局配置.f模式_接口配置("f0/0")	#进入接口FastEthernet0/0
	v接口配置.fs网络地址4("1.1.1.1/24", a操作 = 脚本.E操作.e设置)	#设置地址
	v接口配置.fs开关(True)	#开启接口
if __name__ == "__main__":
	main()
```
## 文档
[参考](文档/参考.md)包含网络设备脚本的应用程序接口的详细信息

[操作](文档/操作.md)介绍了每种操作能达到怎样的效果