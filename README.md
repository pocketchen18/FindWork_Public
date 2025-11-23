# Yingjiesheng Job Application Automation

This project automates the process of applying for internships on the Yingjiesheng (应届生) website using Playwright for browser automation.

## Overview

The script automates the following tasks:
- Navigates to the Yingjiesheng internship search page
- Searches for specified positions
- Automatically clicks "立即申请" (Apply Now) buttons for multiple listings
- Handles different types of application popups and new windows
- Supports pagination for applying to more positions than fit on one page

## Features

- **Automated Job Search**: Fill in position requirements and automatically search
- **Bulk Application**: Apply to multiple positions in one run
- **Popup Handling**: Automatically handles different types of application popups
- **Pagination Support**: Automatically navigates to next pages when needed
- **Browser Automation**: Uses Firefox browser through Playwright

## Prerequisites

- Python 3.7+
- Playwright library
- Firefox browser

## Installation

1. Install the required dependencies:
   ```bash
   pip install playwright
   ```

2. Install Playwright's browser drivers:
   ```bash
   playwright install firefox
   ```

## Usage

1. Run the script:
   ```bash
   python -m core.mian
   ```

2. Follow the prompts:
   - Press Enter to continue through initialization steps
   - Enter the position you want to search for
   - Specify how many applications you want to submit

## How It Works

The automation script:

1. Opens Firefox browser in non-headless mode
2. Navigates to the Yingjiesheng internship search page
3. Waits for user input for position type
4. Fills the search field and submits the search
5. Counts and clicks "立即申请" (Apply Now) buttons
6. Handles both new window applications and popup modals
7. Automatically paginates to continue applying through multiple pages

## Important Notes

- This script is designed to run in non-headless mode so you can monitor the automation
- The script includes timeouts and error handling for robust operation
- Make sure you're logged in to Yingjiesheng before running the script if required
- Use responsibly and in accordance with the website's terms of service

## Project Structure

```
/workspace/
├── README.md
└── core/
    ├── __init__.py
    ├── mian.py          # Main entry point
    └── utils/
        ├── __init__.py
        └── yingjiesheng_findwork.py  # Core automation logic
```

## Customization

You can modify the `yingjiesheng_findwork.py` file to:
- Change the XPath selectors if the website layout changes
- Adjust wait times and timeouts
- Add additional application logic

## License

This project is available as-is without any warranty. Please use responsibly and in accordance with applicable terms of service.

# 应届生求职自动化申请

本项目使用 Playwright 浏览器自动化技术，自动完成在应届生网站上的实习职位申请流程。

## 概述

该脚本自动化以下任务：
- 导航到应届生实习职位搜索页面
- 搜索指定职位
- 自动点击多个职位列表的“立即申请”按钮
- 处理不同类型的申请弹窗和新窗口
- 支持分页功能，可申请超过单页显示数量的职位

## 功能特点

- **自动化职位搜索**：填写职位要求并自动搜索
- **批量申请**：一次运行可申请多个职位
- **弹窗处理**：自动处理不同类型的申请弹窗
- **分页支持**：自动导航到下一页（如需要）
- **浏览器自动化**：通过 Playwright 使用 Firefox 浏览器

## 系统要求

- Python 3.7+
- Playwright 库
- Firefox 浏览器

## 安装

1. 安装所需依赖：
   ```bash
   pip install playwright
   ```

2. 安装 Playwright 的浏览器驱动：
   ```bash
   playwright install firefox
   ```

## 使用方法

1. 运行脚本：
   ```bash
   python -m core.mian
   ```

2. 按提示操作：
   - 按 Enter 键继续初始化步骤
   - 输入要搜索的职位名称
   - 指定要提交的申请数量

## 工作原理

自动化脚本执行以下操作：

1. 以非无头模式打开 Firefox 浏览器
2. 导航到应届生实习职位搜索页面
3. 等待用户输入职位类型
4. 填写搜索字段并提交搜索
5. 计算并点击“立即申请”按钮
6. 处理新窗口申请和弹窗模式
7. 自动分页以继续申请多个页面的职位

## 重要注意事项

- 该脚本设计为非无头模式运行，以便监控自动化过程
- 脚本包含超时和错误处理以确保稳定运行
- 如需要，请在运行脚本前登录应届生网站
- 请负责任地使用，并遵守网站的服务条款

## 项目结构

```
/workspace/
├── README.md
└── core/
    ├── __init__.py
    ├── mian.py          # 主入口点
    └── utils/
        ├── __init__.py
        └── yingjiesheng_findwork.py  # 核心自动化逻辑
```

## 自定义

您可以修改 `yingjiesheng_findwork.py` 文件来：
- 如果网站布局发生变化，更改 XPath 选择器
- 调整等待时间和超时时间
- 添加额外的申请逻辑

## 许可证

本项目按原样提供，不提供任何保证。请负责任地使用，并遵守适用的服务条款。