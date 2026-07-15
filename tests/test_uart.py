"""
UART驱动单元测试

演示如何测试串行通信驱动
"""

import pytest
from firmware.src.uart import UART


class TestUARTBasic:
    """UART基本功能测试"""

    def test_uart_initialization(self, uart_mock):
        """
        测试UART初始化
        
        验证UART可以正确初始化并进入就绪状态
        """
        uart = UART(device=uart_mock, baudrate=9600)
        assert uart.is_ready() is True
        assert uart.baudrate == 9600

    def test_uart_send(self, uart_mock):
        """
        测试UART发送数据
        
        验证数据正确发送到硬件
        """
        uart = UART(device=uart_mock, baudrate=9600)
        
        test_data = b"Hello, STM32!"
        bytes_sent = uart.send(test_data)
        
        assert bytes_sent == len(test_data)
        assert uart_mock.get_sent_data() == test_data

    def test_uart_receive(self, uart_mock):
        """
        测试UART接收数据
        
        验证可以正确接收硬件发送的数据
        """
        uart = UART(device=uart_mock, baudrate=9600)
        
        # 模拟接收数据
        test_data = b"Response"
        uart_mock.set_receive_data(test_data)
        
        received = uart.receive(len(test_data))
        assert received == test_data

    def test_uart_send_string(self, uart_mock):
        """
        测试UART发送字符串
        
        验证字符串可以正确转换并发送
        """
        uart = UART(device=uart_mock, baudrate=9600)
        
        message = "Test Message"
        uart.send_string(message)
        
        assert uart_mock.get_sent_data() == message.encode('utf-8')


class TestUARTBaudrate:
    """UART波特率测试"""

    @pytest.mark.parametrize("baudrate", [9600, 19200, 38400, 57600, 115200])
    def test_uart_different_baudrates(self, uart_mock, baudrate):
        """
        测试不同的波特率
        
        验证UART支持常见的波特率
        """
        uart = UART(device=uart_mock, baudrate=baudrate)
        assert uart.baudrate == baudrate

    def test_uart_baudrate_change(self, uart_mock):
        """
        测试更改波特率
        
        验证可以动态更改UART的波特率
        """
        uart = UART(device=uart_mock, baudrate=9600)
        assert uart.baudrate == 9600
        
        uart.set_baudrate(115200)
        assert uart.baudrate == 115200


class TestUARTBuffer:
    """UART缓冲区测试"""

    def test_uart_send_multiple_messages(self, uart_mock):
        """
        测试连续发送多条消息
        
        验证缓冲区能正确处理多条消息
        """
        uart = UART(device=uart_mock, baudrate=9600)
        
        messages = [b"MSG1", b"MSG2", b"MSG3"]
        for msg in messages:
            uart.send(msg)
        
        assert uart_mock.get_sent_count() == len(messages)

    def test_uart_receive_buffer(self, uart_mock):
        """
        测试接收缓冲区
        
        验证接收缓冲区能正确处理数据
        """
        uart = UART(device=uart_mock, baudrate=9600)
        
        # 模拟接收多个数据包
        data1 = b"Part1"
        data2 = b"Part2"
        uart_mock.set_receive_data(data1 + data2)
        
        received1 = uart.receive(len(data1))
        received2 = uart.receive(len(data2))
        
        assert received1 == data1
        assert received2 == data2


class TestUARTError:
    """UART错误处理测试"""

    def test_uart_send_empty_data(self, uart_mock):
        """
        测试发送空数据
        
        验证能正确处理空数据的情况
        """
        uart = UART(device=uart_mock, baudrate=9600)
        
        bytes_sent = uart.send(b"")
        assert bytes_sent == 0

    def test_uart_not_initialized(self, uart_mock):
        """
        测试未初始化的UART操作
        
        验证能检测到UART未就绪的状态
        """
        uart = UART(device=uart_mock, baudrate=9600)
        uart.close()  # 关闭UART
        
        assert uart.is_ready() is False
        assert uart.send(b"test") == -1
