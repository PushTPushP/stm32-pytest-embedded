"""
LED驱动模块 - Python实现版本用于测试

在实际STM32项目中，这会是C代码。
这个版本用于演示如何编写可测试的代码。
"""


class LED:
    """
    LED驱动类
    
    提供LED的基本控制功能：开启、关闭、切换、亮度控制等
    """
    
    def __init__(self, pin):
        """
        初始化LED对象
        
        Args:
            pin (int): GPIO引脚号
        """
        self.pin = pin
        self._state = False  # LED初始状态为关闭
        self._brightness = 0  # PWM亮度 0-255
        self._blinking = False
        self._blink_interval = 0
    
    def on(self):
        """打开LED"""
        self._state = True
        self._brightness = 255
    
    def off(self):
        """关闭LED"""
        self._state = False
        self._brightness = 0
    
    def toggle(self):
        """切换LED状态"""
        if self._state:
            self.off()
        else:
            self.on()
    
    def is_on(self):
        """
        获取LED状态
        
        Returns:
            bool: True表示LED开启，False表示关闭
        """
        return self._state
    
    def set_brightness(self, value):
        """
        设置LED亮度（PWM）
        
        Args:
            value (int): 亮度值，范围0-255
        """
        if value < 0:
            value = 0
        elif value > 255:
            value = 255
        
        self._brightness = value
        self._state = (value > 0)
    
    def get_brightness(self):
        """
        获取LED亮度
        
        Returns:
            int: 当前亮度值 0-255
        """
        return self._brightness
    
    def start_blink(self, interval):
        """
        开始LED闪烁
        
        Args:
            interval (int): 闪烁间隔（毫秒）
        """
        self._blinking = True
        self._blink_interval = interval
    
    def stop_blink(self):
        """停止LED闪烁"""
        self._blinking = False
        self._blink_interval = 0
    
    def is_blinking(self):
        """
        检查LED是否在闪烁
        
        Returns:
            bool: True表示在闪烁，False表示未闪烁
        """
        return self._blinking
