.PHONY: help test test-verbose test-cov test-unit test-integration lint format clean install docs

# 默认target
.DEFAULT_GOAL := help

# 帮助信息
help:
	@echo "STM32 pytest嵌入式测试项目 - 可用命令:"
	@echo ""
	@echo "安装:"
	@echo "  make install          - 安装所有依赖"
	@echo ""
	@echo "测试:"
	@echo "  make test             - 运行所有测试"
	@echo "  make test-verbose     - 详细输出运行所有测试"
	@echo "  make test-cov         - 运行测试并生成覆盖率报告"
	@echo "  make test-unit        - 仅运行单元测试"
	@echo "  make test-integration - 仅运行集成测试"
	@echo ""
	@echo "代码质量:"
	@echo "  make lint             - 运行pylint检查"
	@echo "  make format           - 使用black格式化代码"
	@echo ""
	@echo "清理:"
	@echo "  make clean            - 清理临时文件"
	@echo ""

# 安装依赖
install:
	pip install -r requirements.txt

test:
	pytest

test-verbose:
	pytest -v

test-cov:
	pytest --cov=firmware --cov=mocks --cov-report=html --cov-report=term

test-unit:
	pytest -m unit -v

test-integration:
	pytest -m integration -v

lint:
	pylint firmware/ tests/ mocks/ || true

format:
	black firmware/ tests/ mocks/ --line-length=100

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	rm -rf .coverage htmlcov/ 2>/dev/null || true

clean-all: clean
	rm -rf venv/

dev-setup: install
	pip install ipython jupyter notebook
