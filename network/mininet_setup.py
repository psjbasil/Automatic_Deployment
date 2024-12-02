# network/mininet_setup.py
from mininet.net import Mininet
from mininet.node import OVSSwitch, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel


def create_network():
    """创建一个包含多个交换机和主机的Mininet网络"""
    # 设置日志级别
    setLogLevel('info')

    # 创建网络实例
    net = Mininet(controller=RemoteController, switch=OVSSwitch)

    # 添加控制器
    c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633)

    # 创建交换机
    s1, s2, s3 = [net.addSwitch(f's{i + 1}') for i in range(3)]

    # 创建主机
    h1, h2, h3, h4 = [net.addHost(f'h{i + 1}') for i in range(4)]

    # 连接设备
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(s1, s2)
    net.addLink(s2, s3)
    net.addLink(h3, s3)
    net.addLink(h4, s3)

    # 启动网络
    net.start()

    # 打开CLI供用户交互
    CLI(net)

    # 停止网络
    net.stop()


if __name__ == '__main__':
    create_network()