import json


TASK_DESCRIPTION = "专属AI助手，擅长日常对话和简单问答"


prompt = f"""
请生成50条用于微调大模型的训练数据，任务类型：{TASK_DESCRIPTION}

要求：
1. 每条数据包含 instruction（指令）、input（输入，可为空）、output（输出）
2. 问题类型要多样化（问候、问答、任务执行等）
3. 输出要自然、友好
4. 严格按照JSON格式返回

示例格式：
[
    {{"instruction": "请做自我介绍", "input": "", "output": "你好，我是AI助手..."}},
    {{"instruction": "回答问题", "input": "今天天气如何", "output": "今天天气晴朗..."}}
]

请直接返回JSON数组，不要其他说明文字。
"""

print(prompt)
print("\n" + "="*50)
print("将上面的提示词复制到 ChatGPT/通义千问/文心一言 等对话框")
print("然后把返回的JSON保存为 data/my_train.json")
