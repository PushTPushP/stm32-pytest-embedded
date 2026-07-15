# STM32/ARM嵌入式系统pytest测试框架

一个完整的嵌入式系统测试学习项目，展示如何在STM32/ARM开发中应用pytest进行单元测试、集成测试和硬件模拟。

## 📚 项目目标

- ✅ 学会在嵌入式开发中使用pytest框架
- ✅ 掌握C/C++代码的单元测试方法
- ✅ 理解硬件模拟(Mock)和依赖注入
- ✅ 实现CI/CD自动化测试
- ✅ 编写可测试的嵌入式代码架构

## 🏗️ 项目结构

```
stm32-pytest-embedded/
├── firmware/                 # 嵌入式固件代码
│   ├── src/                 # 源代码
│   │   ├── led.c/h          # LED驱动示例
│   │   ├── uart.c/h         # UART驱动示例
│   │   ├── button.c/h       # 按钮驱动示例
│   │   └── system.c/h       # 系统初始化
│   └── hal/                 # STM32 HAL库模拟
│       └── stm32_hal_mock.h # HAL库Mock定义
│
├── tests/                    # pytest测试套件
│   ├── test_led.py          # LED单元测试
│   ├── test_uart.py         # UART单元测试
│   ├── test_button.py       # 按钮单元测试
│   ├── test_integration.py  # 集成测试
│   └── conftest.py          # pytest配置和fixtures
│
├── mocks/                    # 硬件模拟库
│   ├── __init__.py
│   ├── gpio_mock.py         # GPIO模拟
│   ├── uart_mock.py         # UART模拟
│   └── timer_mock.py        # 定时器模拟
│
├── docs/                     # 学习文档
│   ├── 01_pytest入门.md     # pytest基础教程
│   ├── 02_嵌入式测试指南.md # 嵌入式测试最佳实践
│   ├── 03_Mock和依赖注入.md # Mock框架使用
│   └── 04_CI-CD配置.md      # GitHub Actions配置
│
├── .github/
│   └── workflows/
│       └── pytest.yml       # GitHub Actions自动测试
│
├── pytest.ini               # pytest配置文件
├── requirements.txt         # Python依赖
├── CMakeLists.txt          # C/C++构建配置
└── Makefile                # 便利命令
```

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行所有测试

```bash
pytest
```

### 3. 运行特定测试

```bash
# 运行LED测试
pytest tests/test_led.py -v

# 运行并显示详细输出
pytest tests/ -v --tb=short

# 生成覆盖率报告
pytest --cov=firmware tests/
```

### 4. 查看学习文档

详见 `docs/` 目录中的各个教程。

## 📖 学习路径

### 初级：pytest基础
1. 阅读 `docs/01_pytest入门.md`
2. 运行 `tests/test_led.py` - 理解基本单元测试
3. 修改LED驱动代码，观察测试结果

### 中级：嵌入式测试
1. 阅读 `docs/02_嵌入式测试指南.md`
2. 学习 `tests/test_uart.py` - 处理复杂的硬件交互
3. 学习 `tests/test_button.py` - 事件驱动测试

### 高级：Mock和架构
1. 阅读 `docs/03_Mock和依赖注入.md`
2. 学习 `mocks/` 目录中的实现
3. 阅读 `tests/test_integration.py` - 集成测试

### 生产级：CI/CD
1. 阅读 `docs/04_CI-CD配置.md`
2. 观察 `.github/workflows/pytest.yml` 运行
3. 修改代码，自动触发测试

## 🔧 核心概念

### 1. 单元测试 (Unit Testing)
```python
def test_led_on():
    """测试LED开启功能"""
    led = LED(pin=13)
    led.on()
    assert led.is_on() == True
```

### 2. Mock硬件
```python
def test_uart_send(uart_mock):
    """使用Mock测试UART发送"""
    uart = UART(uart_mock.get_interface())
    uart.send("Hello")
    assert uart_mock.get_data_sent() == b"Hello"
```

### 3. 依赖注入
```python
def test_button_with_callback(button_driver, callback_mock):
    """通过依赖注入进行测试"""
    button = Button(driver=button_driver, callback=callback_mock)
    button.press()
    callback_mock.assert_called_once()
```

### 4. 集成测试
```python
def test_system_initialization(system):
    """测试整个系统初始化流程"""
    system.init()
    assert system.led.is_ready()
    assert system.uart.is_ready()
    assert system.button.is_ready()
```

## 📊 测试覆盖率

```bash
pytest --cov=firmware --cov-report=html tests/
```

生成的报告在 `htmlcov/index.html`

## 🔄 CI/CD工作流

每次提交时自动运行：
- ✅ 代码格式检查 (pylint)
- ✅ 所有单元测试
- ✅ 覆盖率检查
- ✅ 集成测试

## 💡 最佳实践

1. **编写可测试的代码**
   - 使用依赖注入而非全局变量
   - 将硬件抽象为接口
   - 分离业务逻辑和硬件驱动

2. **充分的单元测试**
   - 每个函数至少一个测试
   - 测试正常情况和边界情况
   - 使用Mock隔离外部依赖

3. **清晰的测试命名**
   - `test_<function>_<scenario>_<expected_result>`
   - 例如：`test_led_on_when_pin_is_high`

4. **使用fixtures**
   - 复用测试设置代码
   - 自动清理资源
   - 提高测试可读性

## 📚 参考资源

- [pytest官方文档](https://docs.pytest.org/)
- [STM32CubeMX](https://www.st.com/en/development-tools/stm32cubemx.html)
- [单元测试最佳实践](https://en.wikipedia.org/wiki/Unit_testing)
- [嵌入式系统测试](https://www.embedded.com/)

## 🤝 贡献

欢迎提交Issue和Pull Request来改进这个学习项目。

## 📄 许可证

MIT License - 自由使用和修改

## 🎯 下一步

1. 🔍 浏览 `firmware/src/` 中的驱动代码
2. ✍️ 运行 `pytest tests/ -v` 查看测试结果
3. 📖 读 `docs/01_pytest入门.md` 学习基础
4. 🛠️ 修改代码，自己编写测试

---

**开始学习嵌入式测试了吗？** 快速开始指南见上方 🚀
