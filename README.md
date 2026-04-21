# MCP (Model Context Protocol) 模型上下文协议 实践项目

基于 **FastMCP** 实现的本地 MCP 服务端，集成计算器、桌面文件获取工具，支持 CherryAI 客户端 / 手写 Python 客户端连接调用，完成 MCP 服务端与客户端全流程联调。

## 项目简介

本项目是 MCP（模型上下文协议）的实践 Demo，**自主编写 MCP 服务端**，提供可调用的工具函数，并通过客户端完成连接、调用、数据返回的完整流程，验证 MCP 协议的通信能力。

## 技术栈

- Python 3.13+
- FastMCP（MCP 服务端框架）
- MCP 协议

## 项目结构

```
mcp-demo/
├── text.py           # MCP 服务端（核心，提供工具接口）
├── mcp_client.py     # 手写 Python MCP 客户端
├── requirements.txt  # 项目依赖声明
├── .gitignore        # Git 忽略文件
└── README.md         # 项目说明文档
```

## 核心功能（服务端工具）

1. 计算器工具 (`calculator`)

   - 支持加减乘除四则运算
   - 输入参数：数字 a、数字 b、运算符 (+/-/*//)

   

2. 桌面文件获取工具 (`get_desktop_files`)

   - 获取 Windows 电脑桌面的所有文件 / 文件夹列表
   - 无输入参数，直接调用返回结果

## 环境安装

1. 克隆 / 下载项目到本地
2. 安装项目依赖

```
pip install -r requirements.txt
```

## 使用教程

### 方式 1：CherryAI 客户端连接（推荐，可视化调用）

1. 打开 CherryAI → 进入 **MCP 服务器** 配置面板
2. 新建 MCP 服务端配置：
   - Transport Type：`STDIO`
   - Command：`D:\anaconda\envs\MCP\python.exe`（虚拟环境 Python 路径）
   - Arguments：`E:\CLASS\big_modle\MCP\text.py`（服务端文件绝对路径）
3. 点击 `Connect`，显示 **已连接 / 已激活** 即为成功
4. 聊天窗口发送指令调用工具：

```
调用本地MCP计算器工具，计算 10 + 20
调用本地MCP工具获取桌面文件列表
```

### 方式 2：手写 Python 客户端调用

无需手动启动服务端，直接运行客户端

```
python mcp_client.py
```

客户端自动启动服务端、连接、调用工具并打印结果
