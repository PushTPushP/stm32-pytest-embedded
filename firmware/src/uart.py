"""
UART驱动模块

提供串行通信的基本功能：初始化、发送、接收等
"""


class UART:
    """
    UART驱动类
    
    管理串行通信
    """
    
    def __init__(self, device, baudrate=9600):
        """
        初始化UART
        
        Args:
            device: UART设备接口（或Mock对象）
            baudrate (int): 波特率
        """
        self.device = device
        self.baudrate = baudrate
        self._ready = True
        self._sent_data = b""
        self._receive_buffer = b""
    
    def is_ready(self):
        """
        检查UART是否就绪
        
        Returns:
            bool: True表示就绪，False表示未就绪
        """
        return self._ready
    
    def send(self, data):
        """
        发送数据
        
        Args:
            data (bytes): 要发送的数据
        
        Returns:
            int: 实际发送的字节数，-1表示错误
        """
        if not self._ready:
            return -1
        
        if not data:
            return 0
        
        self._sent_data = data
        self.device.send(data)
        return len(data)
    
    def receive(self, length):
        """
        接收数据
        
        Args:
            length (int): 要接收的字节数
        
        Returns:
            bytes: 接收到的数据
        """
        if not self._ready:
            return b""
        
        return self.device.receive(length)
    
    def send_string(self, string):
        """
        发送字符串
        
        Args:
            string (str): 要发送的字符串
        
        Returns:
            int: 发送的字节数
        """
        data = string.encode('utf-8')
        return self.send(data)
    
    def set_baudrate(self, baudrate):
        """
        设置波特率
        
        Args:
            baudrate (int): 新的波特率
        """
        self.baudrate = baudrate
    
    def close(self):
        """关闭UART"""
        self._ready = False
    
    def reinit(self):
        """重新初始化UART"""
        self._ready = True
