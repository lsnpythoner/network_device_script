import enum
class E模式(enum.IntEnum):
	"适用于: mw155r"
	e运行状态 = 0
	e设置向导 = 1
	eWPS一键安全设定 = 2
	e网络参数 = 3
	e网络参数_WAN口设置 = 4
	e网络参数_WWAN口速率模式 = 5
	e网络参数_WLAN口设置 = 6
	e网络参数_WMAC地址克隆 = 7
	e无线设置 = 8
	e无线设置_基本设置 = 9
	e无线设置_无线安全设置 = 10
	e无线设置_无线MAC地址过滤 = 11
	e无线设置_无线高级设置 = 12
	e无线设置_主机状态 = 13
	eDHCP服务器 = 14
	eDHCP服务器_DHCP服务 = 15
	eDHCP服务器_客户端列表 = 16
	eDHCP服务器_静态地址分配 = 17
	e转发规则 = 18
	e转发规则_虚拟服务器 = 19
	e转发规则_DMZ主机 = 20
	e转发规则_UPnP设置 = 21
	e安全功能 = 22
	e安全功能_局域网WEB管理 = 23
	e安全功能_远程WEB管理 = 24
	e家长控制 = 25
	e家长控制_上网控制 = 26
	e家长控制_规则管理 = 27
	e家长控制_主机列表 = 28
	e家长控制_访问目标 = 29
	e家长控制_日程计划 = 30
	e路由功能 = 31
	e路由功能_静态路由表 = 32
	e路由功能_系统路由表 = 33
	eIP带宽控制 = 34
	eIP与MAC绑定 = 35
	eIP与MAC绑定_静态ARP绑定设置 = 36
	eIP与MAC绑定_ARP映射表 = 37
	e动态DNS = 38
	e系统工具 = 39
	e系统工具_时间设置 = 40
	e系统工具_诊断工具 = 41
	e系统工具_软件升级 = 42
	e系统工具_恢复出厂设置 = 43
	e系统工具_备份和载入配置 = 44
	e系统工具_重启路由器 = 45
	e系统工具_修改登录密码 = 46
	e系统工具_系统日志 = 47
	e系统工具_流量统计 = 48
class C模式:
	"适用于: mw155r"
	c运行状态 = (0,)
	c设置向导 = (1,)
	cWPS一键安全设定 = (2,)
	c网络参数 = (3,)
	c网络参数_WAN口设置 = (3, 4)
	c网络参数_WWAN口速率模式 = (3, 5)
	c网络参数_WLAN口设置 = (3, 6)
	c网络参数_WMAC地址克隆 = (3, 7)
	c无线设置 = (8,)
	c无线设置_基本设置 = (8, 9)
	c无线设置_无线安全设置 = (8, 10)
	c无线设置_无线MAC地址过滤 = (8, 11)
	c无线设置_无线高级设置 = (8, 12)
	c无线设置_主机状态 = (8, 13)
	cDHCP服务器 = (14,)
	cDHCP服务器_DHCP服务 = (14, 15)
	cDHCP服务器_客户端列表 = (14, 16)
	cDHCP服务器_静态地址分配 = (14, 17)
	c转发规则 = (18,)
	c转发规则_虚拟服务器 = (18, 19)
	c转发规则_DMZ主机 = (18, 20)
	c转发规则_UPnP设置 = (18, 21)
	c安全功能 = (22,)
	c安全功能_局域网WEB管理 = (22, 23)
	c安全功能_远程WEB管理 = (22, 24)
	c家长控制 = (25,)
	c家长控制_上网控制 = (25, 26)
	c家长控制_规则管理 = (25, 27)
	c家长控制_主机列表 = (25, 28)
	c家长控制_访问目标 = (25, 29)
	c家长控制_日程计划 = (25, 30)
	c路由功能 = (31,)
	c路由功能_静态路由表 = (31, 32)
	c路由功能_系统路由表 = (31, 33)
	cIP带宽控制 = (34,)
	cIP与MAC绑定 = (35,)
	cIP与MAC绑定_静态ARP绑定设置 = (35, 36)
	cIP与MAC绑定_ARP映射表 = (35, 37)
	c动态DNS = (38,)
	c系统工具 = (39,)
	c系统工具_时间设置 = (39, 40)
	c系统工具_诊断工具 = (39, 41)
	c系统工具_软件升级 = (39, 42)
	c系统工具_恢复出厂设置 = (39, 43)
	c系统工具_备份和载入配置 = (39, 44)
	c系统工具_重启路由器 = (39, 45)
	c系统工具_修改登录密码 = (39, 46)
	c系统工具_系统日志 = (39, 47)
	c系统工具_流量统计 = (39, 48)
