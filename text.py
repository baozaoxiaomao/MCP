import os
from mcp.server.fastmcp import FastMCP

# 服务名称
mcp = FastMCP("FileSystem")

# 自定义工具1：获取桌面文件
@mcp.tool()
def get_desktop_files() -> list:
    '''获取当前用户的桌面文件列表'''
    return os.listdir(os.path.expanduser("~/Desktop"))

# 自定义工具2：计算器
@mcp.tool()
def calculator(a: float, b: float, operator: str) -> float:
    """执行基础数学运算(支持+-*/)
    Args:
        operator: 运算符,必须是'+','-','*','/'之一
    """
    if operator == '+': return a + b
    elif operator == '-': return a - b
    elif operator == '*': return a * b
    elif operator == '/': return a / b
    else: raise ValueError("无效运算符")

if __name__ == "__main__":
    # 标准输入输出通信
    mcp.run(transport='stdio')