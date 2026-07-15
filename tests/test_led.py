"""
LED驱动单元测试

演示如何使用pytest进行基本的嵌入式硬件驱动测试
"""

import pytest
from firmware.src.led import LED


class TestLEDBasic:
    """LED基本功能测试"""

    def test_led_initialization(self):
        """
        测试LED初始化
        
        验证LED对象可以正确创建并初始状态为关闭
        """
        led = LED(pin=13)
        assert led.pin == 13
        assert led.is_on() is False

    def test_led_on(self):
        """
        测试LED开启功能
        
        验证调用on()方法后LED状态为开启
        """
        led = LED(pin=13)
        led.on()
        assert led.is_on() is True

    def test_led_off(self):
        """
        测试LED关闭功能
        
        验证调用off()方法后LED状态为关闭
        """
        led = LED(pin=13)
        led.on()
        assert led.is_on() is True
        
        led.off()
        assert led.is_on() is False

    def test_led_toggle(self):
        """
        测试LED切换功能
        
        验证toggle()方法能正确切换LED状态
        """
        led = LED(pin=13)
        
        # 初始状态为关
        assert led.is_on() is False
        
        # 切换到开
        led.toggle()
        assert led.is_on() is True
        
        # 再切换到关
        led.toggle()
        assert led.is_on() is False


class TestLEDWithMock:
    """使用Mock的LED测试"""

    def test_led_brightness(self):
        """
        测试LED亮度设置
        
        验证PWM亮度值在0-255范围内
        """
        led = LED(pin=13)
        
        # 设置不同的亮度
        led.set_brightness(0)    # 最暗
        assert led.get_brightness() == 0
        
        led.set_brightness(128)  # 中等亮度
        assert led.get_brightness() == 128
        
        led.set_brightness(255)  # 最亮
        assert led.get_brightness() == 255

    def test_led_brightness_boundary(self):
        """
        测试LED亮度边界条件
        
        验证亮度值在边界时的处理
        """
        led = LED(pin=13)
        
        # 测试最小值
        led.set_brightness(-1)
        assert led.get_brightness() == 0  # 应该被限制到0
        
        # 测试最大值
        led.set_brightness(256)
        assert led.get_brightness() == 255  # 应该被限制到255

    def test_led_blink(self):
        """
        测试LED闪烁功能
        
        验证闪烁状态和间隔
        """
        led = LED(pin=13)
        
        # 开始闪烁
        led.start_blink(interval=100)  # 100ms间隔
        assert led.is_blinking() is True
        
        # 停止闪烁
        led.stop_blink()
        assert led.is_blinking() is False


class TestLEDMultiple:
    """多个LED的测试"""

    def test_multiple_leds(self):
        """
        测试多个LED对象独立工作
        
        验证不同LED的状态互不影响
        """
        led1 = LED(pin=13)
        led2 = LED(pin=14)
        led3 = LED(pin=15)
        
        # 分别控制LED
        led1.on()
        led2.off()
        led3.toggle()
        
        # 验证状态
        assert led1.is_on() is True
        assert led2.is_on() is False
        assert led3.is_on() is True

    def test_led_get_pin(self):
        """
        测试LED获取引脚号
        """
        pins = [13, 14, 15, 16, 17]
        leds = [LED(pin=p) for p in pins]
        
        for led, pin in zip(leds, pins):
            assert led.pin == pin


# 参数化测试示例
@pytest.mark.parametrize("pin,expected", [
    (13, True),
    (14, False),
    (15, True),
])
def test_led_parametrized(pin, expected):
    """
    参数化测试LED
    
    使用不同的参数运行同一个测试
    """
    led = LED(pin=pin)
    if expected:
        led.on()
    else:
        led.off()
    assert led.is_on() == expected
