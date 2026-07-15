"""
Timer Mock实现

模拟STM32的定时器接口
"""

import time


class TimerMock:
    """
    定时器模拟类
    
    模拟定时器的基本功能
    """
    
    def __init__(self):
        """
        初始化Timer Mock
        """
        self.running = False
        self.interval = 0
        self.start_time = 0
        self.elapsed_time = 0
    
    def start(self, interval):
        """
        启动定时器
        
        Args:
            interval (int): 定时时间（毫秒）
        """
        self.running = True
        self.interval = interval
        self.start_time = time.time()
        self.elapsed_time = 0
    
    def stop(self):
        """停止定时器"""
        self.running = False
    
    def is_running(self):
        """
        检查定时器是否运行中
        
        Returns:
            bool: True表示运行中，False表示未运行
        """
        return self.running
    
    def is_elapsed(self):
        """
        检查定时是否到期
        
        Returns:
            bool: True表示已到期，False表示未到期
        """
        if not self.running:
            return False
        
        current_elapsed = (time.time() - self.start_time) * 1000 + self.elapsed_time
        return current_elapsed >= self.interval
    
    def get_elapsed(self):
        """
        获取已经过的时间
        
        Returns:
            int: 已经过的时间（毫秒）
        """
        if not self.running:
            return 0
        
        return int((time.time() - self.start_time) * 1000 + self.elapsed_time)
    
    def tick(self, milliseconds):
        """
        模拟时间流逝
        
        Args:
            milliseconds (int): 流逝的毫秒数
        """
        self.elapsed_time += milliseconds
