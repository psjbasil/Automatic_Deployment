# tests/test_network.py
import unittest
from subprocess import Popen, PIPE

class TestNetwork(unittest.TestCase):
    def test_mininet_setup(self):
        """测试Mininet网络设置"""
        process = Popen(["python3", "network/mininet_setup.py"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, error = process.communicate(input=b'exit\n')
        self.assertIn(b'*** Mininet is exiting', output)

if __name__ == '__main__':
    unittest.main()