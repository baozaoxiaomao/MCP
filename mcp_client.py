import asyncio
from fastmcp import FastMCPClient

async def main():

    client = FastMCPClient(
        command="python",
        args=["text.py"]
    )

    try:
        # 连接
        await client.connect()
        print("="*50)
        print("✅ 手写客户端 成功连接自己的MCP服务端！")
        print("="*50)

        # 调用计算器工具
        result = await client.call_tool("calculator", a=10, b=20, operator="+")
        print(f"\n🧮 10 + 20 = {result}")

        print("\n🎉 测试完成！")

    finally:
        await client.close()

if __name__ == "__main__":
    asyncio.run(main())
