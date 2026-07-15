"""
pytest配置文件

定义全局fixtures和配置，供所有测试使用
"""

import pytest
import sys
from pathlib import Path

# 添加项目根目录到Python路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from mocks.gpio_mock import GPIOMock
from mocks.uart_mock import UARTMock
from mocks.timer_mock import TimerMock


# ==================== 基础Fixtures ====================

@pytest.fixture(scope="function")
def gpio_mock():
    """
    提供GPIO Mock对象
    
    使用示例:
        def test_something(gpio_mock):
            gpio_mock.set_pin(13, True)
            assert gpio_mock.read_pin(13) == True
    """
    return GPIOMock()


@pytest.fixture(scope="function")
def uart_mock():
    """
    提供UART Mock对象
    
    使用示例:
        def test_uart(uart_mock):
            uart_mock.send(b"Hello")
            data = uart_mock.receive(5)
            assert data == b"Hello"
    """
    return UARTMock()


@pytest.fixture(scope="function")
def timer_mock():
    """
    提供Timer Mock对象
    
    使用示例:
        def test_timer(timer_mock):
            timer_mock.start(1000)  # 1秒
            timer_mock.tick(500)    # 500ms
            assert timer_mock.is_elapsed() == False
    """
    return TimerMock()


# ==================== 系统级Fixtures ====================

@pytest.fixture(scope="session")
def test_data_dir():
    """
    返回测试数据目录
    """
    data_dir = Path(__file__).parent / "test_data"
    data_dir.mkdir(exist_ok=True)
    return data_dir


# ==================== Hooks ====================

def pytest_configure(config):
    """
    pytest启动时的配置钩子
    """
    # 注册自定义标记
    config.addinivalue_line(
        "markers", "unit: 标记为单元测试"
    )
    config.addinivalue_line(
        "markers", "integration: 标记为集成测试"
    )
    config.addinivalue_line(
        "markers", "slow: 标记为慢速测试"
    )


def pytest_collection_modifyitems(config, items):
    """
    修改收集到的测试项目
    """
    for item in items:
        # 给没有标记的测试自动标记为unit
        if "integration" not in item.keywords:
            item.add_marker(pytest.mark.unit)
