1.本模块提供百度网盘免会员在线解压功能函数
2.使用方法，新建name.py文件，与bdwp.py放在同一目录下
3.在name.py中import bdwp 便可导入模块，

BAIDUID,BDUSS:
这两个参数确定了百度网盘用户ID和密钥，这两个参数通过抓包获得
具体方式(移动设备用浏览器登录百度网盘网页版，打开抓包工具，抓取浏览器数据包，刷新已登录页面，停止抓包，分析抓到的数据包，这两个参数都在Cookie中，很容易找到)


=======================================
函数调用了requests urllib模块
所以没有安装这两个模块的需要安装

===================================


2018.6.6更新:
将模块由函数形式转变为Class

模块组成:
class Bdwp(BAIDUID,BDUSS)
#用BAIDUID,BDUSS完成实例化
--def jy(Path,[timeout])
  #解压压缩文件:
  #Path:文件路径 必选参数
  #timeout:请求等待时间 可选，默认3s
  #不建议将timeout设置过短！！
  #返回:无
--def ls(Path)
	#获取传入路径文件列表:
	#Path:路径
	#返回:list型数据，列表形式如下
	 [ {
      "category": 6,
      "unlist": 0,
      "fs_id": 553522009033918,
      "dir_empty": 0,
      "oper_id": 2762369205,
      "server_ctime": 1527411314,
      "local_mtime": 1527411314,
      "size": 0,
      "share": 0,
      "isdir": 1,
      "path": "/2018老男孩9期",
      "local_ctime": 1527411314,
      "server_filename": "2018老男孩9期",
      "empty": 0,
      "server_mtime": 1527572909
    },
    {
      "category": 6,
      "unlist": 0,
      "fs_id": 1056398897286807,
      "dir_empty": 0,
      "oper_id": 2762369205,
      "server_ctime": 1523641728,
      "local_mtime": 1523641728,
      "size": 0,
      "share": 0,
      "isdir": 1,
      "path": "/python3全栈",
      "local_ctime": 1523641728,
      "server_filename": "python3全栈",
      "empty": 0,
      "server_mtime": 1523642547
    }]